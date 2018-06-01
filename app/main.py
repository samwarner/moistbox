import time
import datetime
import bme680
import maya


def main():
    sensor = bme680.BME680()
    # These oversampling settings can be tweaked to
    # change the balance between accuracy and noise in
    # the data.

    sensor.set_humidity_oversample(bme680.OS_2X)
    sensor.set_pressure_oversample(bme680.OS_4X)
    sensor.set_temperature_oversample(bme680.OS_8X)
    sensor.set_filter(bme680.FILTER_SIZE_3)

    print("Polling:")
    try:
        while True:
            if sensor.get_sensor_data():
                now = maya.MayaDT.from_struct(time.gmtime())
                t = sensor.data.temperature
                h = sensor.data.humidity
                p = sensor.data.pressure
                output = f"{now} - Temp: {t:.2f} C, Hum: {h:.2f} HU, Pres: {p:.2f} hPa."

                print(output)

                time.sleep(60)

    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    # execute only if run as a script
    main()
