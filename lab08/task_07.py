import logging

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

prices = [120, 80.5, 49.5]
total = sum(prices)

logging.info("Количество цен: %s", len(prices))
logging.info("Общая стоимость: %s", total)
