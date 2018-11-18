import os
import datetime
from App.Repository import *
from helpers import generate_unique_code, hash_password
# from Orgs.models import OrganisationUser, OrgTypeOrg, OrgTypeOrgUser
from models import User, UserToken


##
# AuthRepository - For all database transactions
##
class AuthRepository():

    ##
    # To Store the data
    ##
    def store(self, model, data):
        result = store(model, data)
        return result

    def update(self, model, filterBy, data):
        result = update(model, filterBy, data)
        return result

    def fetch_all(self, model):
        result = fetchAll(model)
        return result

    def filter_attribute(self, model, findBy):
        result = filter_attribute(model, findBy).first()
        return result

    def delete(self, model, findBy):
        result = delete(model, findBy)
        return result


class UserTokenRepository():

    def store(self, model, data):
        '''
        ' To Store the data
        '''
        result = store(model, data)
        return result

    def check_valid_token(self, model, token):
        '''
        check valid token
        '''
        findBy = {
            'token': token,
        }
        result = filter_attribute(model, findBy).filter(
            model.expires_at > datetime.datetime.now()).first()
        return result

    def deleteToken(self, model, token):
        '''
        delete token
        '''
        return delete(model, {'token': token})
