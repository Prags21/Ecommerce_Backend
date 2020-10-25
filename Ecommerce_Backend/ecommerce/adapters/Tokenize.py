import python_jwt as jwt, jwcrypto.jwk as jwk, datetime
from ..entities.auth import Auth

class TokenGenerator:
    def createToken(auth):
        key = jwk.JWK.generate(kty='RSA', size=2048)
        token = jwt.generate_jwt(auth.__dict__, key, 'PS256', datetime.timedelta(hours=24))

    def getData(token):
        header, claims = jwt.verify_jwt(token, key, ['PS256'])
        print(header)
        print(claims)

auth = Auth()
Tokenize = TokenGenerator()
tok = Tokenize.createToken()
