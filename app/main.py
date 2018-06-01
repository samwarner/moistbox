import time
import bme680


def main():
    sensor = bme680.BME680()
    # These oversampling settings can be tweaked to
    # change the balance between accuracy and noise in
    # the data.

    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)

    print("Poling:")
    try:
        while True:
            if sensor.get_sensor_data():
                output = f"Temp.: {sensor.data.temperature:.2f} C, Hum.: {sensor.data.pressure:.2f} HU, Pres.: {sensor.data.humidity:.2f} hPa."

            print(output)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    # execute only if run as a script
    main()
