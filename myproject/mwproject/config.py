SECRET_KEY= 'oldgrtesy23'
class Config(object):
    MERCHANT_ID= '2345237'

class TestEnviroment(Config):
    MERCHANT_ID = '234567869'
    DBCONN = "Db connection"


class ProductionEnviroment(Config):
    MERCHANT_ID = 'abvnnn'

