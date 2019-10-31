// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    /// <summary>
    /// &gt; This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_snapshot.html.markdown.
    /// </summary>
    public partial class Snapshot : Pulumi.CustomResource
    {
        [Output("creationTimestamp")]
        public Output<string> CreationTimestamp { get; private set; } = null!;

        [Output("description")]
        public Output<string?> Description { get; private set; } = null!;

        [Output("diskSizeGb")]
        public Output<int> DiskSizeGb { get; private set; } = null!;

        [Output("labelFingerprint")]
        public Output<string> LabelFingerprint { get; private set; } = null!;

        [Output("labels")]
        public Output<ImmutableDictionary<string, string>?> Labels { get; private set; } = null!;

        [Output("licenses")]
        public Output<ImmutableArray<string>> Licenses { get; private set; } = null!;

        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        [Output("snapshotEncryptionKey")]
        public Output<Outputs.SnapshotSnapshotEncryptionKey?> SnapshotEncryptionKey { get; private set; } = null!;

        [Output("snapshotId")]
        public Output<int> SnapshotId { get; private set; } = null!;

        [Output("sourceDisk")]
        public Output<string> SourceDisk { get; private set; } = null!;

        [Output("sourceDiskEncryptionKey")]
        public Output<Outputs.SnapshotSourceDiskEncryptionKey?> SourceDiskEncryptionKey { get; private set; } = null!;

        [Output("sourceDiskLink")]
        public Output<string> SourceDiskLink { get; private set; } = null!;

        [Output("storageBytes")]
        public Output<int> StorageBytes { get; private set; } = null!;

        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a Snapshot resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public Snapshot(string name, SnapshotArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/snapshot:Snapshot", name, args, MakeResourceOptions(options, ""))
        {
        }

        private Snapshot(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/snapshot:Snapshot", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing Snapshot resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static Snapshot Get(string name, Input<string> id, SnapshotState? state = null, CustomResourceOptions? options = null)
        {
            return new Snapshot(name, id, state, options);
        }
    }

    public sealed class SnapshotArgs : Pulumi.ResourceArgs
    {
        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        [Input("snapshotEncryptionKey")]
        public Input<Inputs.SnapshotSnapshotEncryptionKeyArgs>? SnapshotEncryptionKey { get; set; }

        [Input("sourceDisk", required: true)]
        public Input<string> SourceDisk { get; set; } = null!;

        [Input("sourceDiskEncryptionKey")]
        public Input<Inputs.SnapshotSourceDiskEncryptionKeyArgs>? SourceDiskEncryptionKey { get; set; }

        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public SnapshotArgs()
        {
        }
    }

    public sealed class SnapshotState : Pulumi.ResourceArgs
    {
        [Input("creationTimestamp")]
        public Input<string>? CreationTimestamp { get; set; }

        [Input("description")]
        public Input<string>? Description { get; set; }

        [Input("diskSizeGb")]
        public Input<int>? DiskSizeGb { get; set; }

        [Input("labelFingerprint")]
        public Input<string>? LabelFingerprint { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        [Input("licenses")]
        private InputList<string>? _licenses;
        public InputList<string> Licenses
        {
            get => _licenses ?? (_licenses = new InputList<string>());
            set => _licenses = value;
        }

        [Input("name")]
        public Input<string>? Name { get; set; }

        /// <summary>
        /// The ID of the project in which the resource belongs.
        /// If it is not provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        [Input("snapshotEncryptionKey")]
        public Input<Inputs.SnapshotSnapshotEncryptionKeyGetArgs>? SnapshotEncryptionKey { get; set; }

        [Input("snapshotId")]
        public Input<int>? SnapshotId { get; set; }

        [Input("sourceDisk")]
        public Input<string>? SourceDisk { get; set; }

        [Input("sourceDiskEncryptionKey")]
        public Input<Inputs.SnapshotSourceDiskEncryptionKeyGetArgs>? SourceDiskEncryptionKey { get; set; }

        [Input("sourceDiskLink")]
        public Input<string>? SourceDiskLink { get; set; }

        [Input("storageBytes")]
        public Input<int>? StorageBytes { get; set; }

        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public SnapshotState()
        {
        }
    }

    namespace Inputs
    {

    public sealed class SnapshotSnapshotEncryptionKeyArgs : Pulumi.ResourceArgs
    {
        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        [Input("sha256")]
        public Input<string>? Sha256 { get; set; }

        public SnapshotSnapshotEncryptionKeyArgs()
        {
        }
    }

    public sealed class SnapshotSnapshotEncryptionKeyGetArgs : Pulumi.ResourceArgs
    {
        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        [Input("sha256")]
        public Input<string>? Sha256 { get; set; }

        public SnapshotSnapshotEncryptionKeyGetArgs()
        {
        }
    }

    public sealed class SnapshotSourceDiskEncryptionKeyArgs : Pulumi.ResourceArgs
    {
        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        public SnapshotSourceDiskEncryptionKeyArgs()
        {
        }
    }

    public sealed class SnapshotSourceDiskEncryptionKeyGetArgs : Pulumi.ResourceArgs
    {
        [Input("rawKey")]
        public Input<string>? RawKey { get; set; }

        public SnapshotSourceDiskEncryptionKeyGetArgs()
        {
        }
    }
    }

    namespace Outputs
    {

    [OutputType]
    public sealed class SnapshotSnapshotEncryptionKey
    {
        public readonly string? RawKey;
        public readonly string Sha256;

        [OutputConstructor]
        private SnapshotSnapshotEncryptionKey(
            string? rawKey,
            string sha256)
        {
            RawKey = rawKey;
            Sha256 = sha256;
        }
    }

    [OutputType]
    public sealed class SnapshotSourceDiskEncryptionKey
    {
        public readonly string? RawKey;

        [OutputConstructor]
        private SnapshotSourceDiskEncryptionKey(string? rawKey)
        {
            RawKey = rawKey;
        }
    }
    }
}
