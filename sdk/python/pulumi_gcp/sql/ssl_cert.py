# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from .. import utilities, tables

class SslCert(pulumi.CustomResource):
    cert: pulumi.Output[str]
    """
    The actual certificate data for this client certificate.
    """
    cert_serial_number: pulumi.Output[str]
    """
    The serial number extracted from the certificate data.
    """
    common_name: pulumi.Output[str]
    """
    The common name to be used in the certificate to identify the
    client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
    """
    create_time: pulumi.Output[str]
    """
    The time when the certificate was created in RFC 3339 format,
    for example 2012-11-15T16:19:00.094Z.
    """
    expiration_time: pulumi.Output[str]
    """
    The time when the certificate expires in RFC 3339 format,
    for example 2012-11-15T16:19:00.094Z.
    """
    instance: pulumi.Output[str]
    """
    The name of the Cloud SQL instance. Changing this
    forces a new resource to be created.
    """
    private_key: pulumi.Output[str]
    """
    The private key associated with the client certificate.
    """
    project: pulumi.Output[str]
    """
    The ID of the project in which the resource belongs. If it
    is not provided, the provider project is used.
    """
    server_ca_cert: pulumi.Output[str]
    """
    The CA cert of the server this client cert was generated from.
    """
    sha1_fingerprint: pulumi.Output[str]
    """
    The SHA1 Fingerprint of the certificate.
    """
    def __init__(__self__, resource_name, opts=None, common_name=None, instance=None, project=None, __name__=None, __opts__=None):
        """
        Creates a new Google SQL SSL Cert on a Google SQL Instance. For more information, see the [official documentation](https://cloud.google.com/sql/), or the [JSON API](https://cloud.google.com/sql/docs/mysql/admin-api/v1beta4/sslCerts).
        
        > **Note:** All arguments including the private key will be stored in the raw state as plain-text.
        [Read more about sensitive data in state](https://www.terraform.io/docs/state/sensitive-data.html).
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] common_name: The common name to be used in the certificate to identify the
               client. Constrained to [a-zA-Z.-_ ]+. Changing this forces a new resource to be created.
        :param pulumi.Input[str] instance: The name of the Cloud SQL instance. Changing this
               forces a new resource to be created.
        :param pulumi.Input[str] project: The ID of the project in which the resource belongs. If it
               is not provided, the provider project is used.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/sql_ssl_cert.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if common_name is None:
            raise TypeError("Missing required property 'common_name'")
        __props__['common_name'] = common_name

        if instance is None:
            raise TypeError("Missing required property 'instance'")
        __props__['instance'] = instance

        __props__['project'] = project

        __props__['cert'] = None
        __props__['cert_serial_number'] = None
        __props__['create_time'] = None
        __props__['expiration_time'] = None
        __props__['private_key'] = None
        __props__['server_ca_cert'] = None
        __props__['sha1_fingerprint'] = None

        super(SslCert, __self__).__init__(
            'gcp:sql/sslCert:SslCert',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

