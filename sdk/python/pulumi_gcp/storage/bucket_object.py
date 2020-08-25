# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Dict, List, Mapping, Optional, Tuple, Union
from .. import _utilities, _tables

__all__ = ['BucketObject']


class BucketObject(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bucket: Optional[pulumi.Input[str]] = None,
                 cache_control: Optional[pulumi.Input[str]] = None,
                 content: Optional[pulumi.Input[str]] = None,
                 content_disposition: Optional[pulumi.Input[str]] = None,
                 content_encoding: Optional[pulumi.Input[str]] = None,
                 content_language: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 detect_md5hash: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = None,
                 storage_class: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        Creates a new object inside an existing bucket in Google cloud storage service (GCS).
        [ACLs](https://cloud.google.com/storage/docs/access-control/lists) can be applied using the `storage.ObjectACL` resource.
         For more information see
        [the official documentation](https://cloud.google.com/storage/docs/key-terms#objects)
        and
        [API](https://cloud.google.com/storage/docs/json_api/v1/objects).

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the containing bucket.
        :param pulumi.Input[str] cache_control: [Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
               directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600
        :param pulumi.Input[str] content: Data as `string` to be uploaded. Must be defined if `source` is not. **Note**: The `content` field is marked as sensitive.
        :param pulumi.Input[str] content_disposition: [Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.
        :param pulumi.Input[str] content_encoding: [Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.
        :param pulumi.Input[str] content_language: [Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.
        :param pulumi.Input[str] content_type: [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: User-provided metadata, in key/value pairs.
        :param pulumi.Input[str] name: The name of the object. If you're interpolating the name of this object, see `output_name` instead.
        :param pulumi.Input[Union[pulumi.Asset, pulumi.Archive]] source: A path to the data you want to upload. Must be defined
               if `content` is not.
        :param pulumi.Input[str] storage_class: The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
               Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`. If not provided, this defaults to the bucket's default
               storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = dict()

            if bucket is None:
                raise TypeError("Missing required property 'bucket'")
            __props__['bucket'] = bucket
            __props__['cache_control'] = cache_control
            __props__['content'] = content
            __props__['content_disposition'] = content_disposition
            __props__['content_encoding'] = content_encoding
            __props__['content_language'] = content_language
            __props__['content_type'] = content_type
            __props__['detect_md5hash'] = detect_md5hash
            __props__['metadata'] = metadata
            __props__['name'] = name
            __props__['source'] = source
            __props__['storage_class'] = storage_class
            __props__['crc32c'] = None
            __props__['md5hash'] = None
            __props__['media_link'] = None
            __props__['output_name'] = None
            __props__['self_link'] = None
        super(BucketObject, __self__).__init__(
            'gcp:storage/bucketObject:BucketObject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            bucket: Optional[pulumi.Input[str]] = None,
            cache_control: Optional[pulumi.Input[str]] = None,
            content: Optional[pulumi.Input[str]] = None,
            content_disposition: Optional[pulumi.Input[str]] = None,
            content_encoding: Optional[pulumi.Input[str]] = None,
            content_language: Optional[pulumi.Input[str]] = None,
            content_type: Optional[pulumi.Input[str]] = None,
            crc32c: Optional[pulumi.Input[str]] = None,
            detect_md5hash: Optional[pulumi.Input[str]] = None,
            md5hash: Optional[pulumi.Input[str]] = None,
            media_link: Optional[pulumi.Input[str]] = None,
            metadata: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
            name: Optional[pulumi.Input[str]] = None,
            output_name: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            source: Optional[pulumi.Input[Union[pulumi.Asset, pulumi.Archive]]] = None,
            storage_class: Optional[pulumi.Input[str]] = None) -> 'BucketObject':
        """
        Get an existing BucketObject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] bucket: The name of the containing bucket.
        :param pulumi.Input[str] cache_control: [Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
               directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600
        :param pulumi.Input[str] content: Data as `string` to be uploaded. Must be defined if `source` is not. **Note**: The `content` field is marked as sensitive.
        :param pulumi.Input[str] content_disposition: [Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.
        :param pulumi.Input[str] content_encoding: [Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.
        :param pulumi.Input[str] content_language: [Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.
        :param pulumi.Input[str] content_type: [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".
        :param pulumi.Input[str] crc32c: (Computed) Base 64 CRC32 hash of the uploaded data.
        :param pulumi.Input[str] md5hash: (Computed) Base 64 MD5 hash of the uploaded data.
        :param pulumi.Input[str] media_link: (Computed) A url reference to download this object.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] metadata: User-provided metadata, in key/value pairs.
        :param pulumi.Input[str] name: The name of the object. If you're interpolating the name of this object, see `output_name` instead.
        :param pulumi.Input[str] output_name: (Computed) The name of the object. Use this field in interpolations with `storage.ObjectACL` to recreate
               `storage.ObjectACL` resources when your `storage.BucketObject` is recreated.
        :param pulumi.Input[str] self_link: (Computed) A url reference to this object.
        :param pulumi.Input[Union[pulumi.Asset, pulumi.Archive]] source: A path to the data you want to upload. Must be defined
               if `content` is not.
        :param pulumi.Input[str] storage_class: The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
               Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`. If not provided, this defaults to the bucket's default
               storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["bucket"] = bucket
        __props__["cache_control"] = cache_control
        __props__["content"] = content
        __props__["content_disposition"] = content_disposition
        __props__["content_encoding"] = content_encoding
        __props__["content_language"] = content_language
        __props__["content_type"] = content_type
        __props__["crc32c"] = crc32c
        __props__["detect_md5hash"] = detect_md5hash
        __props__["md5hash"] = md5hash
        __props__["media_link"] = media_link
        __props__["metadata"] = metadata
        __props__["name"] = name
        __props__["output_name"] = output_name
        __props__["self_link"] = self_link
        __props__["source"] = source
        __props__["storage_class"] = storage_class
        return BucketObject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def bucket(self) -> str:
        """
        The name of the containing bucket.
        """
        return pulumi.get(self, "bucket")

    @property
    @pulumi.getter(name="cacheControl")
    def cache_control(self) -> Optional[str]:
        """
        [Cache-Control](https://tools.ietf.org/html/rfc7234#section-5.2)
        directive to specify caching behavior of object data. If omitted and object is accessible to all anonymous users, the default will be public, max-age=3600
        """
        return pulumi.get(self, "cache_control")

    @property
    @pulumi.getter
    def content(self) -> Optional[str]:
        """
        Data as `string` to be uploaded. Must be defined if `source` is not. **Note**: The `content` field is marked as sensitive.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="contentDisposition")
    def content_disposition(self) -> Optional[str]:
        """
        [Content-Disposition](https://tools.ietf.org/html/rfc6266) of the object data.
        """
        return pulumi.get(self, "content_disposition")

    @property
    @pulumi.getter(name="contentEncoding")
    def content_encoding(self) -> Optional[str]:
        """
        [Content-Encoding](https://tools.ietf.org/html/rfc7231#section-3.1.2.2) of the object data.
        """
        return pulumi.get(self, "content_encoding")

    @property
    @pulumi.getter(name="contentLanguage")
    def content_language(self) -> Optional[str]:
        """
        [Content-Language](https://tools.ietf.org/html/rfc7231#section-3.1.3.2) of the object data.
        """
        return pulumi.get(self, "content_language")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        [Content-Type](https://tools.ietf.org/html/rfc7231#section-3.1.1.5) of the object data. Defaults to "application/octet-stream" or "text/plain; charset=utf-8".
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def crc32c(self) -> str:
        """
        (Computed) Base 64 CRC32 hash of the uploaded data.
        """
        return pulumi.get(self, "crc32c")

    @property
    @pulumi.getter(name="detectMd5hash")
    def detect_md5hash(self) -> Optional[str]:
        return pulumi.get(self, "detect_md5hash")

    @property
    @pulumi.getter
    def md5hash(self) -> str:
        """
        (Computed) Base 64 MD5 hash of the uploaded data.
        """
        return pulumi.get(self, "md5hash")

    @property
    @pulumi.getter(name="mediaLink")
    def media_link(self) -> str:
        """
        (Computed) A url reference to download this object.
        """
        return pulumi.get(self, "media_link")

    @property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, str]]:
        """
        User-provided metadata, in key/value pairs.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the object. If you're interpolating the name of this object, see `output_name` instead.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputName")
    def output_name(self) -> str:
        """
        (Computed) The name of the object. Use this field in interpolations with `storage.ObjectACL` to recreate
        `storage.ObjectACL` resources when your `storage.BucketObject` is recreated.
        """
        return pulumi.get(self, "output_name")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        (Computed) A url reference to this object.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def source(self) -> Optional[Union[pulumi.Asset, pulumi.Archive]]:
        """
        A path to the data you want to upload. Must be defined
        if `content` is not.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="storageClass")
    def storage_class(self) -> str:
        """
        The [StorageClass](https://cloud.google.com/storage/docs/storage-classes) of the new bucket object.
        Supported values include: `MULTI_REGIONAL`, `REGIONAL`, `NEARLINE`, `COLDLINE`, `ARCHIVE`. If not provided, this defaults to the bucket's default
        storage class or to a [standard](https://cloud.google.com/storage/docs/storage-classes#standard) class.
        """
        return pulumi.get(self, "storage_class")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

