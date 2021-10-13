import tensorflow as tf

model = tf.keras.models.load_model('Data/Emotion_Recognition/model.h5')
converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()
open("ERModel.tflite", "wb").write(tflite_model)
