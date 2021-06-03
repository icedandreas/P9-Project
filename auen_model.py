from keras.models import Model, Sequential
from keras.layers import Conv1D, UpSampling1D, MaxPooling1D
from keras.layers import Input, Flatten, Reshape, Dense, Dropout
from performance_meter import measure_and_print_performance

NUM_FILTERS, FILTER_LENGTH1, FILTER_LENGTH2 = 32, 8, 4 # [8, 12], [4, 8]

def molecule_model_CNN_CNN(model_name, NUM_FILTERS, FILTER_LENGTH):
    # Encoder
    # drug = Input(shape=(100, 64))
    drug = Input(shape=(100, 1))

    encoded = Conv1D(filters=NUM_FILTERS, kernel_size=FILTER_LENGTH, activation='relu', input_shape=(None, ))(drug)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH, activation='relu')(encoded)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*3, kernel_size=FILTER_LENGTH, activation='relu')(encoded)
    encoded = MaxPooling1D()(encoded)

    encoded = Flatten()(encoded)
    encoded = Dense(50, activation='relu')(encoded)

    # Decoder
    decoded = Dense(2976, activation='relu')(encoded)
    decoded = Reshape((31, 96))(decoded)

    decoded = Conv1D(filters=NUM_FILTERS*3, kernel_size=FILTER_LENGTH, activation='relu')(decoded)
    decoded = UpSampling1D()(decoded)
    decoded = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH, activation='relu')(decoded)
    decoded = UpSampling1D()(decoded)
    decoded = Conv1D(filters=1, kernel_size=FILTER_LENGTH, activation='relu')(decoded)
    decoded = UpSampling1D(4)(decoded)
    decoded = Flatten()(decoded)
    decoded = Dense(100, activation='relu')(decoded)
    decoded = Reshape((100, 1))(decoded)
    # decoded = Dense(6400, activation='relu')(decoded)
    # decoded = Reshape((100, 64))(decoded)
    # decoded = Flatten()(decoded)

    autoencoder = Model(inputs=drug, outputs=decoded, name=model_name)

    encoder = Model(inputs=drug, outputs=encoded)

    metrics=['accuracy', 'mean_squared_error']
    autoencoder.compile(optimizer='adam', loss='mean_squared_error', metrics=metrics)

    print(autoencoder.summary())
    return autoencoder, encoder

def molecule_model_CNN_DNN(model_name, NUM_FILTERS, FILTER_LENGTH):
    # Encoder
    # drug = Input(shape=(100, 64))
    drug = Input(shape=(100, 1))
    encoded = Conv1D(filters=NUM_FILTERS, kernel_size=FILTER_LENGTH, activation='relu', input_shape=(None, ))(drug)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH, activation='relu')(encoded)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*3, kernel_size=FILTER_LENGTH, activation='relu')(encoded)
    encoded = MaxPooling1D()(encoded)

    encoded = Flatten()(encoded)
    encoded = Dense(50, activation='relu')(encoded)

    # Decoder
    # decoded = Reshape((10, 5))(encoded)
    # decoded = Dense(1920, activation='sigmoid')(encoded)
    # decoded = Dense(2560, activation='relu')(decoded)
    # decoded = Dense(6400, activation='relu')(decoded)
    # decoded = Reshape((100, 64))(decoded)
    decoded = Dense(70, activation='sigmoid')(encoded)
    decoded = Dense(90, activation='relu')(decoded)
    decoded = Dense(100, activation='relu')(decoded)
    decoded = Reshape((100, 1))(decoded)

    autoencoder = Model(inputs=drug, outputs=decoded, name=model_name)

    encoder = Model(inputs=drug, outputs=encoded)

    metrics=['accuracy', 'mean_squared_error']
    autoencoder.compile(optimizer='adam', loss='mean_squared_error', metrics=metrics)

    print(autoencoder.summary())
    return autoencoder, encoder

def protein_model_CNN_CNN(model_name, NUM_FILTERS, FILTER_LENGTH):
    # Encoder
    # target = Input(shape=(1000, 25))
    target = Input(shape=(1000, 1))
    encoded = Conv1D(filters=NUM_FILTERS, kernel_size=FILTER_LENGTH, activation='relu', input_shape=(None, ))(target)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH, activation='relu')(encoded)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*3, kernel_size=FILTER_LENGTH, activation='sigmoid')(encoded)
    encoded = MaxPooling1D()(encoded)

    encoded = Flatten()(encoded)
    encoded = Dense(30, activation='relu')(encoded)

    # Decoder
    decoded = Dense(864, activation='relu')(encoded)
    decoded = Reshape((9, -1))(decoded)

    decoded = UpSampling1D(4)(decoded)
    decoded = Conv1D(filters=NUM_FILTERS*3, kernel_size=FILTER_LENGTH, activation='sigmoid')(decoded)
    decoded = UpSampling1D()(decoded)
    decoded = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH, activation='relu')(decoded)
    decoded = UpSampling1D()(decoded)
    decoded = Conv1D(filters=1, kernel_size=FILTER_LENGTH, activation='relu')(decoded)
    decoded = Flatten()(decoded)
    decoded = Dense(1000, activation='relu')(decoded)
    decoded = Reshape((1000, 1))(decoded)
    # decoded = Dense(25000, activation='relu')(decoded)
    # decoded = Reshape((1000, 25))(decoded)
    # decoded = Flatten()(decoded)
    
    # decoded = Dense(100, activation='relu')(decoded)
    # decoded = Reshape((100, 1))(decoded)

    autoencoder = Model(inputs=target, outputs=decoded, name=model_name)

    encoder = Model(inputs=target, outputs=encoded)

    metrics=['accuracy', 'mean_squared_error']
    autoencoder.compile(optimizer='adam', loss='mean_squared_error', metrics=metrics)

    print(autoencoder.summary())
    return autoencoder, encoder

def protein_model_CNN_DNN(model_name, NUM_FILTERS, FILTER_LENGTH):
    # Encoder
    target = Input(shape=(1000, 1))
    # target = Input(shape=(1000, 25))
    encoded = Conv1D(filters=NUM_FILTERS, kernel_size=FILTER_LENGTH, activation='relu', input_shape=(None, ))(target)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*2, kernel_size=FILTER_LENGTH, activation='relu')(encoded)
    encoded = MaxPooling1D()(encoded)
    encoded = Conv1D(filters=NUM_FILTERS*3, kernel_size=FILTER_LENGTH, activation='sigmoid')(encoded)
    encoded = MaxPooling1D()(encoded)

    encoded = Flatten()(encoded)
    encoded = Dense(30, activation='relu')(encoded)

    # Decoder
    # decoded = Reshape((10, 3))(encoded)
    # decoded = Dense(1000, activation='sigmoid')(encoded)
    # decoded = Dense(10000, activation='relu')(decoded)
    # decoded = Dense(25000, activation='relu')(decoded)
    # decoded = Reshape((1000, 25))(decoded)
    decoded = Dense(200, activation='sigmoid')(encoded)
    decoded = Dense(500, activation='relu')(decoded)
    decoded = Dense(1000, activation='relu')(decoded)
    decoded = Reshape((1000, 1))(decoded)

    autoencoder = Model(inputs=target, outputs=decoded, name=model_name)

    encoder = Model(inputs=target, outputs=encoded)

    metrics=['accuracy', 'mean_squared_error']
    autoencoder.compile(optimizer='adam', loss='mean_squared_error', metrics=metrics)

    print(autoencoder.summary())
    return autoencoder, encoder

def interaction_model(model_name):
    model = Sequential(name=model_name)

    model.add(Input(shape=(80,)))
    model.add(Dense(700, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(500, activation='sigmoid'))
    model.add(Dropout(0.1))
    model.add(Dense(300, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(100, activation='sigmoid'))
    model.add(Dropout(0.1))
    model.add(Dense(50, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(25, activation='relu'))
    model.add(Dropout(0.1))
    model.add(Dense(1, activation='relu'))

    metrics=['accuracy', 'mean_squared_error']
    model.compile(optimizer='adam', loss='mean_squared_error', metrics=metrics)

    print(model.summary())
    return model

def train_molecule_model(model_name, x_train, x_test, batch_size, epochs, callbacks=None):
    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1).astype('uint8')
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1).astype('uint8')

    mol_autoencoder, mol_encoder = None, None
    if model_name == 'auen_molecule_CNN_CNN':
        mol_autoencoder, mol_encoder = molecule_model_CNN_CNN(model_name, NUM_FILTERS, FILTER_LENGTH1)
        mol_autoencoder.fit(x_train, x_train, batch_size, epochs, callbacks=callbacks)
    elif model_name == 'auen_molecule_CNN_DNN':
        mol_autoencoder, mol_encoder = molecule_model_CNN_DNN(model_name, NUM_FILTERS, FILTER_LENGTH1)
        mol_autoencoder.fit(x_train, x_train, batch_size, epochs, callbacks=callbacks)

    encoded_x_test = mol_encoder.predict(x_test)
    encoded_x_train = mol_encoder.predict(x_train)

    return encoded_x_train, encoded_x_test

def train_protein_model(model_name, x_train, x_test, batch_size, epochs, callbacks=None):
    x_train = x_train.reshape(x_train.shape[0], x_train.shape[1], 1).astype('uint8')
    x_test = x_test.reshape(x_test.shape[0], x_test.shape[1], 1).astype('uint8')

    prot_autoencoder, prot_encoder = None, None
    if model_name == 'auen_protein_CNN_CNN':
        prot_autoencoder, prot_encoder = protein_model_CNN_CNN(model_name, NUM_FILTERS, FILTER_LENGTH2)
        prot_autoencoder.fit(x_train, x_train, batch_size, epochs, callbacks=callbacks)
    elif model_name == 'auen_protein_CNN_DNN':
        prot_autoencoder, prot_encoder = protein_model_CNN_DNN(model_name, NUM_FILTERS, FILTER_LENGTH2)
        prot_autoencoder.fit(x_train, x_train, batch_size, epochs, callbacks=callbacks)

    encoded_x_test = prot_encoder.predict(x_test)
    encoded_x_train = prot_encoder.predict(x_train)

    return encoded_x_train, encoded_x_test

def train_interaction_model(model_name, dataset, batch_size, epochs, callbacks=None):
    model = interaction_model(model_name)
    # print(f'x_train shape: {dataset["x_train"].shape}')
    # print(f'x_train shape: {dataset["y_train"].shape}')
    # x_train = np.array(dataset["x_train"])
    # y_train = np.array(dataset["y_train"])
    # x_test = np.array(dataset["x_test"])
    # y_test = np.array(dataset["y_test"])
    # print(f'x_train shape: {x_train.shape}')
    # print(f'y_train shape: {y_train.shape}')
    model.fit(dataset['x_train'], dataset['y_train'], batch_size, epochs, callbacks=callbacks)
    predictions = model.predict(dataset['x_test'])
    print(measure_and_print_performance(model_name, dataset['name'], dataset['y_test'], predictions.flatten()))
