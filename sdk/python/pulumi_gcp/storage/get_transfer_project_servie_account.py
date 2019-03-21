# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class GetTransferProjectServieAccountResult:
    """
    A collection of values returned by getTransferProjectServieAccount.
    """
    def __init__(__self__, email=None, project=None, id=None):
        if email and not isinstance(email, str):
            raise TypeError('Expected argument email to be a str')
        __self__.email = email
        """
        Email address of the default service account used by Storage Transfer Jobs running in this project
        """
        if project and not isinstance(project, str):
            raise TypeError('Expected argument project to be a str')
        __self__.project = project
        if id and not isinstance(id, str):
            raise TypeError('Expected argument id to be a str')
        __self__.id = id
        """
        id is the provider-assigned unique ID for this managed resource.
        """

async def get_transfer_project_servie_account(project=None,opts=None):
    """
    Use this data source to retrieve Storage Transfer service account for this project
    """
    __args__ = dict()

    __args__['project'] = project
    __ret__ = await pulumi.runtime.invoke('gcp:storage/getTransferProjectServieAccount:getTransferProjectServieAccount', __args__, opts=opts)

    return GetTransferProjectServieAccountResult(
        email=__ret__.get('email'),
        project=__ret__.get('project'),
        id=__ret__.get('id'))
