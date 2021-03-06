# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

# Export this package's modules as members:
from .app_profile import *
from .connection import *
from .data_transfer_config import *
from .dataset import *
from .dataset_access import *
from .dataset_iam_binding import *
from .dataset_iam_member import *
from .dataset_iam_policy import *
from .get_default_service_account import *
from .iam_binding import *
from .iam_member import *
from .iam_policy import *
from .job import *
from .reservation import *
from .routine import *
from .table import *
from ._inputs import *
from . import outputs

def _register_module():
    import pulumi
    from .. import _utilities


    class Module(pulumi.runtime.ResourceModule):
        _version = _utilities.get_semver_version()

        def version(self):
            return Module._version

        def construct(self, name: str, typ: str, urn: str) -> pulumi.Resource:
            if typ == "gcp:bigquery/appProfile:AppProfile":
                return AppProfile(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/connection:Connection":
                return Connection(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/dataTransferConfig:DataTransferConfig":
                return DataTransferConfig(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/dataset:Dataset":
                return Dataset(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/datasetAccess:DatasetAccess":
                return DatasetAccess(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/datasetIamBinding:DatasetIamBinding":
                return DatasetIamBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/datasetIamMember:DatasetIamMember":
                return DatasetIamMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/datasetIamPolicy:DatasetIamPolicy":
                return DatasetIamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/iamBinding:IamBinding":
                return IamBinding(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/iamMember:IamMember":
                return IamMember(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/iamPolicy:IamPolicy":
                return IamPolicy(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/job:Job":
                return Job(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/reservation:Reservation":
                return Reservation(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/routine:Routine":
                return Routine(name, pulumi.ResourceOptions(urn=urn))
            elif typ == "gcp:bigquery/table:Table":
                return Table(name, pulumi.ResourceOptions(urn=urn))
            else:
                raise Exception(f"unknown resource type {typ}")


    _module_instance = Module()
    pulumi.runtime.register_resource_module("gcp", "bigquery/appProfile", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/connection", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/dataTransferConfig", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/dataset", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/datasetAccess", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/datasetIamBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/datasetIamMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/datasetIamPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/iamBinding", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/iamMember", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/iamPolicy", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/job", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/reservation", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/routine", _module_instance)
    pulumi.runtime.register_resource_module("gcp", "bigquery/table", _module_instance)

_register_module()
