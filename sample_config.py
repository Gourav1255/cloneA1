#----------------------------------- https://github.com/m4mallu/clonebot --------------------------------------------#
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)

class Config(object):

    # Get a bot token from botfather
    TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "5632300210:AAH7BJQYJocKeyk_7BIYJsI2j7b0EIw26V0")

    # Get from my.telegram.org
    APP_ID = int(os.environ.get("APP_ID", "19751208"))

    # Get from my.telegram.org
    API_HASH = os.environ.get("API_HASH", "7ee46e0888432fad23173820d4caddf2")

    # Generate a user session string
    TG_USER_SESSION = os.environ.get("TG_USER_SESSION", "BQCG-ZV9vEGRfhOA4ypxIP6U93qZ0xWZII2v9LMNjM8saGQ3FOxm1u3n-OG2gsYLSSMk1DoxSSc1BBYcSgazuNibp41Wl6_QemSVIBLmnUeQ9LiWpFnyQG6xVqnyvCjJp1wxEcp8BeHJTrlc3Tz6SE0GI0oKrSEGZQ3qIOkU4hnTJze02Gnfd5KkKzdtSowYo0gNU0UXdtH2DdJEKROtN4M8pqMvqyRzb-r33J6vYXUS8hgv1K_7I-XYfcfmFX4HmZUb6IjEeaO7aTlDmXxsIpqbaITilnMzOOHEZboPBq7PTZNsPJJHoCEm2YADPbuX2NeP1jkwVM5ZcEEIdZ2_aHwPcSgHPgA")

    # Database URI
    DB_URI = os.environ.get("DATABASE_URL", "")


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
