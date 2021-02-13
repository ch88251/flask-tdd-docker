"""
Created by Charles F. Hayes
Date Created: Feb 12, 2021
No rights reserved. Use as you wish.
"""
class BaseConfig:
    """
    Configurations that are common for all environments
    """
    TESTING = False
    DEBUG = False


class DevelopmentConfig(BaseConfig):
    """
    Configurations that are specific for the development environment
    """
    DEBUG = True

class TestingConfig(BaseConfig):
    """
    Configurations that are specific for the testing environment
    """
    TESTING = True


class ProductionConfig(BaseConfig):
    """
    Configurations that are specific for the production environment
    """
