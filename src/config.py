"""
Created by Charles F. Hayes
Date Created: Feb 12, 2021
No rights reserved. Use as you wish.
"""
import os


class BaseConfig:
    """
    Configurations that are common for all environments
    """
    TESTING = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfig(BaseConfig):
    """
    Configurations that are specific for the development environment
    """
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_DEV_URL')


class TestingConfig(BaseConfig):
    """
    Configurations that are specific for the testing environment
    """
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_TEST_URL')


class ProductionConfig(BaseConfig):
    """
    Configurations that are specific for the production environment
    """
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_PROD_URL')
