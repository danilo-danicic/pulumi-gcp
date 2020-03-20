// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    public partial class RegionDisk : Pulumi.CustomResource
    {
        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        [Output("creationTimestamp")]
        public Output<string> CreationTimestamp { get; private set; } = null!;

        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        /// <summary>
        /// Encrypts the disk using a customer-supplied encryption key. After you encrypt a disk with a
        /// customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk
        /// snapshot or an image, or to attach the disk to a virtual machine). Customer-supplied encryption keys do not
        /// protect access to metadata of the disk. If you do not provide an encryption key when creating the disk, then
        /// the disk will be encrypted using an automatically generated key and you do not need to provide a key to use
        /// the disk later.
        /// </summary>
        [Output("diskEncryptionKey")]
        public Output<Outputs.RegionDiskDiskEncryptionKey?> DiskEncryptionKey { get; private set; } = null!;

        /// <summary>
        /// The fingerprint used for optimistic locking of this resource. Used internally during updates.
        /// </summary>
        [Output("labelFingerprint")]
        public Output<string> LabelFingerprint { get; private set; } = null!;

        /// <summary>
        /// Labels to apply to this disk. A list of key-&gt;value pairs.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        /// <summary>
        /// Last attach timestamp in RFC3339 text format.
        /// </summary>
        [Output("lastAttachTimestamp")]
        public Output<string> LastAttachTimestamp { get; private set; } = null!;

        /// <summary>
        /// Last detach timestamp in RFC3339 text format.
        /// </summary>
        [Output("lastDetachTimestamp")]
        public Output<string> LastDetachTimestamp { get; private set; } = null!;

        /// <summary>
        /// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters
        /// long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular
        /// expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all
        /// following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be
        /// a dash.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used.
        /// Currently supported sizes are 4096 and 16384, other sizes may be added in the future. If an unsupported
        /// value is requested, the error message will list the supported values for the caller's project.
        /// </summary>
        [Output("physicalBlockSizeBytes")]
        public Output<int> PhysicalBlockSizeBytes { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// A reference to the region where the disk resides.
        /// </summary>
        [Output("region")]
        public Output<string> Region { get; private set; } = null!;

        /// <summary>
        /// URLs of the zones where the disk should be replicated to.
        /// </summary>
        [Output("replicaZones")]
        public Output<ImmutableArray<string>> ReplicaZones { get; private set; } = null!;

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk
        /// using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.
        /// If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less
        /// than the size of the sourceImage or the size of the snapshot.
        /// </summary>
        [Output("size")]
        public Output<int> Size { get; private set; } = null!;

        /// <summary>
        /// The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.
        /// For example, the following are valid values: *
        /// 'https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot' *
        /// 'projects/project/global/snapshots/snapshot' * 'global/snapshots/snapshot' * 'snapshot'
        /// </summary>
        [Output("snapshot")]
        public Output<string?> Snapshot { get; private set; } = null!;

        /// <summary>
        /// The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by
        /// a customer-supplied encryption key.
        /// </summary>
        [Output("sourceSnapshotEncryptionKey")]
        public Output<Outputs.RegionDiskSourceSnapshotEncryptionKey?> SourceSnapshotEncryptionKey { get; private set; } = null!;

        /// <summary>
        /// The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was
        /// used to create this persistent disk. For example, if you created the persistent disk from a snapshot that
        /// was later deleted and recreated under the same name, the source snapshot ID would identify the exact version
        /// of the snapshot that was used.
        /// </summary>
        [Output("sourceSnapshotId")]
        public Output<string> SourceSnapshotId { get; private set; } = null!;

        /// <summary>
        /// URL of the disk type resource describing which disk type to use to create the disk. Provide this when
        /// creating the disk.
        /// </summary>
        [Output("type")]
        public Output<string?> Type { get; private set; } = null!;

        /// <summary>
        /// Links to the users of the disk (attached instances) in form: project/zones/zone/instances/instance
        /// </summary>
        [Output("users")]
        public Output<ImmutableArray<string>> Users { get; private set; } = null!;


        /// <summary>
        /// Create a RegionDisk resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public RegionDisk(string name, RegionDiskArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/regionDisk:RegionDisk", name, args ?? ResourceArgs.Empty, MakeResourceOptions(options, ""))
        {
        }

        private RegionDisk(string name, Input<string> id, RegionDiskState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/regionDisk:RegionDisk", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing RegionDisk resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static RegionDisk Get(string name, Input<string> id, RegionDiskState? state = null, CustomResourceOptions? options = null)
        {
            return new RegionDisk(name, id, state, options);
        }
    }

    public sealed class RegionDiskArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Encrypts the disk using a customer-supplied encryption key. After you encrypt a disk with a
        /// customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk
        /// snapshot or an image, or to attach the disk to a virtual machine). Customer-supplied encryption keys do not
        /// protect access to metadata of the disk. If you do not provide an encryption key when creating the disk, then
        /// the disk will be encrypted using an automatically generated key and you do not need to provide a key to use
        /// the disk later.
        /// </summary>
        [Input("diskEncryptionKey")]
        public Input<Inputs.RegionDiskDiskEncryptionKeyArgs>? DiskEncryptionKey { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels to apply to this disk. A list of key-&gt;value pairs.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters
        /// long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular
        /// expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all
        /// following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be
        /// a dash.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used.
        /// Currently supported sizes are 4096 and 16384, other sizes may be added in the future. If an unsupported
        /// value is requested, the error message will list the supported values for the caller's project.
        /// </summary>
        [Input("physicalBlockSizeBytes")]
        public Input<int>? PhysicalBlockSizeBytes { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// A reference to the region where the disk resides.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("replicaZones", required: true)]
        private InputList<string>? _replicaZones;

        /// <summary>
        /// URLs of the zones where the disk should be replicated to.
        /// </summary>
        public InputList<string> ReplicaZones
        {
            get => _replicaZones ?? (_replicaZones = new InputList<string>());
            set => _replicaZones = value;
        }

        /// <summary>
        /// Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk
        /// using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.
        /// If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less
        /// than the size of the sourceImage or the size of the snapshot.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.
        /// For example, the following are valid values: *
        /// 'https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot' *
        /// 'projects/project/global/snapshots/snapshot' * 'global/snapshots/snapshot' * 'snapshot'
        /// </summary>
        [Input("snapshot")]
        public Input<string>? Snapshot { get; set; }

        /// <summary>
        /// The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by
        /// a customer-supplied encryption key.
        /// </summary>
        [Input("sourceSnapshotEncryptionKey")]
        public Input<Inputs.RegionDiskSourceSnapshotEncryptionKeyArgs>? SourceSnapshotEncryptionKey { get; set; }

        /// <summary>
        /// URL of the disk type resource describing which disk type to use to create the disk. Provide this when
        /// creating the disk.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        public RegionDiskArgs()
        {
        }
    }

    public sealed class RegionDiskState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// Creation timestamp in RFC3339 text format.
        /// </summary>
        [Input("creationTimestamp")]
        public Input<string>? CreationTimestamp { get; set; }

        /// <summary>
        /// An optional description of this resource. Provide this property when you create the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Encrypts the disk using a customer-supplied encryption key. After you encrypt a disk with a
        /// customer-supplied key, you must provide the same key if you use the disk later (e.g. to create a disk
        /// snapshot or an image, or to attach the disk to a virtual machine). Customer-supplied encryption keys do not
        /// protect access to metadata of the disk. If you do not provide an encryption key when creating the disk, then
        /// the disk will be encrypted using an automatically generated key and you do not need to provide a key to use
        /// the disk later.
        /// </summary>
        [Input("diskEncryptionKey")]
        public Input<Inputs.RegionDiskDiskEncryptionKeyGetArgs>? DiskEncryptionKey { get; set; }

        /// <summary>
        /// The fingerprint used for optimistic locking of this resource. Used internally during updates.
        /// </summary>
        [Input("labelFingerprint")]
        public Input<string>? LabelFingerprint { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// Labels to apply to this disk. A list of key-&gt;value pairs.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// Last attach timestamp in RFC3339 text format.
        /// </summary>
        [Input("lastAttachTimestamp")]
        public Input<string>? LastAttachTimestamp { get; set; }

        /// <summary>
        /// Last detach timestamp in RFC3339 text format.
        /// </summary>
        [Input("lastDetachTimestamp")]
        public Input<string>? LastDetachTimestamp { get; set; }

        /// <summary>
        /// Name of the resource. Provided by the client when the resource is created. The name must be 1-63 characters
        /// long, and comply with RFC1035. Specifically, the name must be 1-63 characters long and match the regular
        /// expression '[a-z]([-a-z0-9]*[a-z0-9])?' which means the first character must be a lowercase letter, and all
        /// following characters must be a dash, lowercase letter, or digit, except the last character, which cannot be
        /// a dash.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// Physical block size of the persistent disk, in bytes. If not present in a request, a default value is used.
        /// Currently supported sizes are 4096 and 16384, other sizes may be added in the future. If an unsupported
        /// value is requested, the error message will list the supported values for the caller's project.
        /// </summary>
        [Input("physicalBlockSizeBytes")]
        public Input<int>? PhysicalBlockSizeBytes { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// A reference to the region where the disk resides.
        /// </summary>
        [Input("region")]
        public Input<string>? Region { get; set; }

        [Input("replicaZones")]
        private InputList<string>? _replicaZones;

        /// <summary>
        /// URLs of the zones where the disk should be replicated to.
        /// </summary>
        public InputList<string> ReplicaZones
        {
            get => _replicaZones ?? (_replicaZones = new InputList<string>());
            set => _replicaZones = value;
        }

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// Size of the persistent disk, specified in GB. You can specify this field when creating a persistent disk
        /// using the sourceImage or sourceSnapshot parameter, or specify it alone to create an empty persistent disk.
        /// If you specify this field along with sourceImage or sourceSnapshot, the value of sizeGb must not be less
        /// than the size of the sourceImage or the size of the snapshot.
        /// </summary>
        [Input("size")]
        public Input<int>? Size { get; set; }

        /// <summary>
        /// The source snapshot used to create this disk. You can provide this as a partial or full URL to the resource.
        /// For example, the following are valid values: *
        /// 'https://www.googleapis.com/compute/v1/projects/project/global/snapshots/snapshot' *
        /// 'projects/project/global/snapshots/snapshot' * 'global/snapshots/snapshot' * 'snapshot'
        /// </summary>
        [Input("snapshot")]
        public Input<string>? Snapshot { get; set; }

        /// <summary>
        /// The customer-supplied encryption key of the source snapshot. Required if the source snapshot is protected by
        /// a customer-supplied encryption key.
        /// </summary>
        [Input("sourceSnapshotEncryptionKey")]
        public Input<Inputs.RegionDiskSourceSnapshotEncryptionKeyGetArgs>? SourceSnapshotEncryptionKey { get; set; }

        /// <summary>
        /// The unique ID of the snapshot used to create this disk. This value identifies the exact snapshot that was
        /// used to create this persistent disk. For example, if you created the persistent disk from a snapshot that
        /// was later deleted and recreated under the same name, the source snapshot ID would identify the exact version
        /// of the snapshot that was used.
        /// </summary>
        [Input("sourceSnapshotId")]
        public Input<string>? SourceSnapshotId { get; set; }

        /// <summary>
        /// URL of the disk type resource describing which disk type to use to create the disk. Provide this when
        /// creating the disk.
        /// </summary>
        [Input("type")]
        public Input<string>? Type { get; set; }

        [Input("users")]
        private InputList<string>? _users;

        /// <summary>
        /// Links to the users of the disk (attached instances) in form: project/zones/zone/instances/instance
        /// </summary>
        public InputList<string> Users
        {
            get => _users ?? (_users = new InputList<string>());
            set => _users = value;
        }

        public RegionDiskState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class RegionDiskDiskEncryptionKeyArgs : Pulumi.ResourceArgs
    {
        [Input("kmsKeyName")]
        public Input<string>? KmsKeyName { get; set; }

        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        [Input("sha256")]
        public Input<string>? Sha256 { get; set; }

        public RegionDiskDiskEncryptionKeyArgs()
        {
        }
    }

    public sealed class RegionDiskDiskEncryptionKeyGetArgs : Pulumi.ResourceArgs
    {
        [Input("kmsKeyName")]
        public Input<string>? KmsKeyName { get; set; }

        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        [Input("sha256")]
        public Input<string>? Sha256 { get; set; }

        public RegionDiskDiskEncryptionKeyGetArgs()
        {
        }
    }

    public sealed class RegionDiskSourceSnapshotEncryptionKeyArgs : Pulumi.ResourceArgs
    {
        [Input("kmsKeyName")]
        public Input<string>? KmsKeyName { get; set; }

        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        [Input("sha256")]
        public Input<string>? Sha256 { get; set; }

        public RegionDiskSourceSnapshotEncryptionKeyArgs()
        {
        }
    }

    public sealed class RegionDiskSourceSnapshotEncryptionKeyGetArgs : Pulumi.ResourceArgs
    {
        [Input("kmsKeyName")]
        public Input<string>? KmsKeyName { get; set; }

        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        [Input("sha256")]
        public Input<string>? Sha256 { get; set; }

        public RegionDiskSourceSnapshotEncryptionKeyGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class RegionDiskDiskEncryptionKey
    {
        public readonly string? KmsKeyName;
        public readonly string? RawKey;
        public readonly string Sha256;

        [OutputConstructor]
        private RegionDiskDiskEncryptionKey(
            string? kmsKeyName,
            string? rawKey,
            string sha256)
        {
            KmsKeyName = kmsKeyName;
            RawKey = rawKey;
            Sha256 = sha256;
        }
    }

    [OutputType]
    public sealed class RegionDiskSourceSnapshotEncryptionKey
    {
        public readonly string? KmsKeyName;
        public readonly string? RawKey;
        public readonly string Sha256;

        [OutputConstructor]
        private RegionDiskSourceSnapshotEncryptionKey(
            string? kmsKeyName,
            string? rawKey,
            string sha256)
        {
            KmsKeyName = kmsKeyName;
            RawKey = rawKey;
            Sha256 = sha256;
        }
    }
    }
}
