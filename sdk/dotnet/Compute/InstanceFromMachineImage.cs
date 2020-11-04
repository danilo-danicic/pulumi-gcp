// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Gcp.Compute
{
    public partial class InstanceFromMachineImage : Pulumi.CustomResource
    {
        /// <summary>
        /// If true, allows Terraform to stop the instance to update its properties. If you try to update a property that requires
        /// stopping the instance without setting this field, the update will fail.
        /// </summary>
        [Output("allowStoppingForUpdate")]
        public Output<bool> AllowStoppingForUpdate { get; private set; } = null!;

        /// <summary>
        /// List of disks attached to the instance
        /// </summary>
        [Output("attachedDisks")]
        public Output<ImmutableArray<Outputs.InstanceFromMachineImageAttachedDisk>> AttachedDisks { get; private set; } = null!;

        /// <summary>
        /// The boot disk for the instance.
        /// </summary>
        [Output("bootDisks")]
        public Output<ImmutableArray<Outputs.InstanceFromMachineImageBootDisk>> BootDisks { get; private set; } = null!;

        /// <summary>
        /// Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
        /// </summary>
        [Output("canIpForward")]
        public Output<bool> CanIpForward { get; private set; } = null!;

        /// <summary>
        /// The Confidential VM config being used by the instance. on_host_maintenance has to be set to TERMINATE or this will fail
        /// to create.
        /// </summary>
        [Output("confidentialInstanceConfig")]
        public Output<Outputs.InstanceFromMachineImageConfidentialInstanceConfig> ConfidentialInstanceConfig { get; private set; } = null!;

        /// <summary>
        /// The CPU platform used by this instance.
        /// </summary>
        [Output("cpuPlatform")]
        public Output<string> CpuPlatform { get; private set; } = null!;

        /// <summary>
        /// Current status of the instance.
        /// </summary>
        [Output("currentStatus")]
        public Output<string> CurrentStatus { get; private set; } = null!;

        /// <summary>
        /// Whether deletion protection is enabled on this instance.
        /// </summary>
        [Output("deletionProtection")]
        public Output<bool> DeletionProtection { get; private set; } = null!;

        /// <summary>
        /// A brief description of the resource.
        /// </summary>
        [Output("description")]
        public Output<string> Description { get; private set; } = null!;

        /// <summary>
        /// Desired status of the instance. Either "RUNNING" or "TERMINATED".
        /// </summary>
        [Output("desiredStatus")]
        public Output<string> DesiredStatus { get; private set; } = null!;

        /// <summary>
        /// Whether the instance has virtual displays enabled.
        /// </summary>
        [Output("enableDisplay")]
        public Output<bool> EnableDisplay { get; private set; } = null!;

        /// <summary>
        /// List of the type and count of accelerator cards attached to the instance.
        /// </summary>
        [Output("guestAccelerators")]
        public Output<ImmutableArray<Outputs.InstanceFromMachineImageGuestAccelerator>> GuestAccelerators { get; private set; } = null!;

        /// <summary>
        /// A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid. Valid format is a series of
        /// labels 1-63 characters long matching the regular expression [a-z]([-a-z0-9]*[a-z0-9]), concatenated with periods. The
        /// entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
        /// </summary>
        [Output("hostname")]
        public Output<string> Hostname { get; private set; } = null!;

        /// <summary>
        /// The server-assigned unique identifier of this instance.
        /// </summary>
        [Output("instanceId")]
        public Output<string> InstanceId { get; private set; } = null!;

        /// <summary>
        /// The unique fingerprint of the labels.
        /// </summary>
        [Output("labelFingerprint")]
        public Output<string> LabelFingerprint { get; private set; } = null!;

        /// <summary>
        /// A set of key/value label pairs assigned to the instance.
        /// </summary>
        [Output("labels")]
        public Output<ImmutableDictionary<string, string>> Labels { get; private set; } = null!;

        /// <summary>
        /// The machine type to create.
        /// </summary>
        [Output("machineType")]
        public Output<string> MachineType { get; private set; } = null!;

        /// <summary>
        /// Metadata key/value pairs made available within the instance.
        /// </summary>
        [Output("metadata")]
        public Output<ImmutableDictionary<string, string>> Metadata { get; private set; } = null!;

        /// <summary>
        /// The unique fingerprint of the metadata.
        /// </summary>
        [Output("metadataFingerprint")]
        public Output<string> MetadataFingerprint { get; private set; } = null!;

        /// <summary>
        /// Metadata startup scripts made available within the instance.
        /// </summary>
        [Output("metadataStartupScript")]
        public Output<string> MetadataStartupScript { get; private set; } = null!;

        /// <summary>
        /// The minimum CPU platform specified for the VM instance.
        /// </summary>
        [Output("minCpuPlatform")]
        public Output<string> MinCpuPlatform { get; private set; } = null!;

        /// <summary>
        /// A unique name for the resource, required by GCE.
        /// Changing this forces a new resource to be created.
        /// </summary>
        [Output("name")]
        public Output<string> Name { get; private set; } = null!;

        /// <summary>
        /// The networks attached to the instance.
        /// </summary>
        [Output("networkInterfaces")]
        public Output<ImmutableArray<Outputs.InstanceFromMachineImageNetworkInterface>> NetworkInterfaces { get; private set; } = null!;

        /// <summary>
        /// The ID of the project in which the resource belongs. If self_link is provided, this value is ignored. If neither
        /// self_link nor project are provided, the provider project is used.
        /// </summary>
        [Output("project")]
        public Output<string> Project { get; private set; } = null!;

        /// <summary>
        /// A list of short names or self_links of resource policies to attach to the instance. Modifying this list will cause the
        /// instance to recreate. Currently a max of 1 resource policy is supported.
        /// </summary>
        [Output("resourcePolicies")]
        public Output<string> ResourcePolicies { get; private set; } = null!;

        /// <summary>
        /// The scheduling strategy being used by the instance.
        /// </summary>
        [Output("scheduling")]
        public Output<Outputs.InstanceFromMachineImageScheduling> Scheduling { get; private set; } = null!;

        /// <summary>
        /// The scratch disks attached to the instance.
        /// </summary>
        [Output("scratchDisks")]
        public Output<ImmutableArray<Outputs.InstanceFromMachineImageScratchDisk>> ScratchDisks { get; private set; } = null!;

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// The service account to attach to the instance.
        /// </summary>
        [Output("serviceAccount")]
        public Output<Outputs.InstanceFromMachineImageServiceAccount> ServiceAccount { get; private set; } = null!;

        /// <summary>
        /// The shielded vm config being used by the instance.
        /// </summary>
        [Output("shieldedInstanceConfig")]
        public Output<Outputs.InstanceFromMachineImageShieldedInstanceConfig> ShieldedInstanceConfig { get; private set; } = null!;

        /// <summary>
        /// Name or self link of a machine
        /// image to create the instance based on.
        /// </summary>
        [Output("sourceMachineImage")]
        public Output<string> SourceMachineImage { get; private set; } = null!;

        /// <summary>
        /// The list of tags attached to the instance.
        /// </summary>
        [Output("tags")]
        public Output<ImmutableArray<string>> Tags { get; private set; } = null!;

        /// <summary>
        /// The unique fingerprint of the tags.
        /// </summary>
        [Output("tagsFingerprint")]
        public Output<string> TagsFingerprint { get; private set; } = null!;

        /// <summary>
        /// The zone that the machine should be created in. If not
        /// set, the provider zone is used.
        /// </summary>
        [Output("zone")]
        public Output<string> Zone { get; private set; } = null!;


        /// <summary>
        /// Create a InstanceFromMachineImage resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public InstanceFromMachineImage(string name, InstanceFromMachineImageArgs args, CustomResourceOptions? options = null)
            : base("gcp:compute/instanceFromMachineImage:InstanceFromMachineImage", name, args ?? new InstanceFromMachineImageArgs(), MakeResourceOptions(options, ""))
        {
        }

        private InstanceFromMachineImage(string name, Input<string> id, InstanceFromMachineImageState? state = null, CustomResourceOptions? options = null)
            : base("gcp:compute/instanceFromMachineImage:InstanceFromMachineImage", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing InstanceFromMachineImage resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static InstanceFromMachineImage Get(string name, Input<string> id, InstanceFromMachineImageState? state = null, CustomResourceOptions? options = null)
        {
            return new InstanceFromMachineImage(name, id, state, options);
        }
    }

    public sealed class InstanceFromMachineImageArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If true, allows Terraform to stop the instance to update its properties. If you try to update a property that requires
        /// stopping the instance without setting this field, the update will fail.
        /// </summary>
        [Input("allowStoppingForUpdate")]
        public Input<bool>? AllowStoppingForUpdate { get; set; }

        /// <summary>
        /// Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
        /// </summary>
        [Input("canIpForward")]
        public Input<bool>? CanIpForward { get; set; }

        /// <summary>
        /// The Confidential VM config being used by the instance. on_host_maintenance has to be set to TERMINATE or this will fail
        /// to create.
        /// </summary>
        [Input("confidentialInstanceConfig")]
        public Input<Inputs.InstanceFromMachineImageConfidentialInstanceConfigArgs>? ConfidentialInstanceConfig { get; set; }

        /// <summary>
        /// Whether deletion protection is enabled on this instance.
        /// </summary>
        [Input("deletionProtection")]
        public Input<bool>? DeletionProtection { get; set; }

        /// <summary>
        /// A brief description of the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Desired status of the instance. Either "RUNNING" or "TERMINATED".
        /// </summary>
        [Input("desiredStatus")]
        public Input<string>? DesiredStatus { get; set; }

        /// <summary>
        /// Whether the instance has virtual displays enabled.
        /// </summary>
        [Input("enableDisplay")]
        public Input<bool>? EnableDisplay { get; set; }

        [Input("guestAccelerators")]
        private InputList<Inputs.InstanceFromMachineImageGuestAcceleratorArgs>? _guestAccelerators;

        /// <summary>
        /// List of the type and count of accelerator cards attached to the instance.
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageGuestAcceleratorArgs> GuestAccelerators
        {
            get => _guestAccelerators ?? (_guestAccelerators = new InputList<Inputs.InstanceFromMachineImageGuestAcceleratorArgs>());
            set => _guestAccelerators = value;
        }

        /// <summary>
        /// A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid. Valid format is a series of
        /// labels 1-63 characters long matching the regular expression [a-z]([-a-z0-9]*[a-z0-9]), concatenated with periods. The
        /// entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// A set of key/value label pairs assigned to the instance.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The machine type to create.
        /// </summary>
        [Input("machineType")]
        public Input<string>? MachineType { get; set; }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// Metadata key/value pairs made available within the instance.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        /// <summary>
        /// Metadata startup scripts made available within the instance.
        /// </summary>
        [Input("metadataStartupScript")]
        public Input<string>? MetadataStartupScript { get; set; }

        /// <summary>
        /// The minimum CPU platform specified for the VM instance.
        /// </summary>
        [Input("minCpuPlatform")]
        public Input<string>? MinCpuPlatform { get; set; }

        /// <summary>
        /// A unique name for the resource, required by GCE.
        /// Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.InstanceFromMachineImageNetworkInterfaceArgs>? _networkInterfaces;

        /// <summary>
        /// The networks attached to the instance.
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageNetworkInterfaceArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.InstanceFromMachineImageNetworkInterfaceArgs>());
            set => _networkInterfaces = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs. If self_link is provided, this value is ignored. If neither
        /// self_link nor project are provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// A list of short names or self_links of resource policies to attach to the instance. Modifying this list will cause the
        /// instance to recreate. Currently a max of 1 resource policy is supported.
        /// </summary>
        [Input("resourcePolicies")]
        public Input<string>? ResourcePolicies { get; set; }

        /// <summary>
        /// The scheduling strategy being used by the instance.
        /// </summary>
        [Input("scheduling")]
        public Input<Inputs.InstanceFromMachineImageSchedulingArgs>? Scheduling { get; set; }

        /// <summary>
        /// The service account to attach to the instance.
        /// </summary>
        [Input("serviceAccount")]
        public Input<Inputs.InstanceFromMachineImageServiceAccountArgs>? ServiceAccount { get; set; }

        /// <summary>
        /// The shielded vm config being used by the instance.
        /// </summary>
        [Input("shieldedInstanceConfig")]
        public Input<Inputs.InstanceFromMachineImageShieldedInstanceConfigArgs>? ShieldedInstanceConfig { get; set; }

        /// <summary>
        /// Name or self link of a machine
        /// image to create the instance based on.
        /// </summary>
        [Input("sourceMachineImage", required: true)]
        public Input<string> SourceMachineImage { get; set; } = null!;

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The list of tags attached to the instance.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The zone that the machine should be created in. If not
        /// set, the provider zone is used.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceFromMachineImageArgs()
        {
        }
    }

    public sealed class InstanceFromMachineImageState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// If true, allows Terraform to stop the instance to update its properties. If you try to update a property that requires
        /// stopping the instance without setting this field, the update will fail.
        /// </summary>
        [Input("allowStoppingForUpdate")]
        public Input<bool>? AllowStoppingForUpdate { get; set; }

        [Input("attachedDisks")]
        private InputList<Inputs.InstanceFromMachineImageAttachedDiskGetArgs>? _attachedDisks;

        /// <summary>
        /// List of disks attached to the instance
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageAttachedDiskGetArgs> AttachedDisks
        {
            get => _attachedDisks ?? (_attachedDisks = new InputList<Inputs.InstanceFromMachineImageAttachedDiskGetArgs>());
            set => _attachedDisks = value;
        }

        [Input("bootDisks")]
        private InputList<Inputs.InstanceFromMachineImageBootDiskGetArgs>? _bootDisks;

        /// <summary>
        /// The boot disk for the instance.
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageBootDiskGetArgs> BootDisks
        {
            get => _bootDisks ?? (_bootDisks = new InputList<Inputs.InstanceFromMachineImageBootDiskGetArgs>());
            set => _bootDisks = value;
        }

        /// <summary>
        /// Whether sending and receiving of packets with non-matching source or destination IPs is allowed.
        /// </summary>
        [Input("canIpForward")]
        public Input<bool>? CanIpForward { get; set; }

        /// <summary>
        /// The Confidential VM config being used by the instance. on_host_maintenance has to be set to TERMINATE or this will fail
        /// to create.
        /// </summary>
        [Input("confidentialInstanceConfig")]
        public Input<Inputs.InstanceFromMachineImageConfidentialInstanceConfigGetArgs>? ConfidentialInstanceConfig { get; set; }

        /// <summary>
        /// The CPU platform used by this instance.
        /// </summary>
        [Input("cpuPlatform")]
        public Input<string>? CpuPlatform { get; set; }

        /// <summary>
        /// Current status of the instance.
        /// </summary>
        [Input("currentStatus")]
        public Input<string>? CurrentStatus { get; set; }

        /// <summary>
        /// Whether deletion protection is enabled on this instance.
        /// </summary>
        [Input("deletionProtection")]
        public Input<bool>? DeletionProtection { get; set; }

        /// <summary>
        /// A brief description of the resource.
        /// </summary>
        [Input("description")]
        public Input<string>? Description { get; set; }

        /// <summary>
        /// Desired status of the instance. Either "RUNNING" or "TERMINATED".
        /// </summary>
        [Input("desiredStatus")]
        public Input<string>? DesiredStatus { get; set; }

        /// <summary>
        /// Whether the instance has virtual displays enabled.
        /// </summary>
        [Input("enableDisplay")]
        public Input<bool>? EnableDisplay { get; set; }

        [Input("guestAccelerators")]
        private InputList<Inputs.InstanceFromMachineImageGuestAcceleratorGetArgs>? _guestAccelerators;

        /// <summary>
        /// List of the type and count of accelerator cards attached to the instance.
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageGuestAcceleratorGetArgs> GuestAccelerators
        {
            get => _guestAccelerators ?? (_guestAccelerators = new InputList<Inputs.InstanceFromMachineImageGuestAcceleratorGetArgs>());
            set => _guestAccelerators = value;
        }

        /// <summary>
        /// A custom hostname for the instance. Must be a fully qualified DNS name and RFC-1035-valid. Valid format is a series of
        /// labels 1-63 characters long matching the regular expression [a-z]([-a-z0-9]*[a-z0-9]), concatenated with periods. The
        /// entire hostname must not exceed 253 characters. Changing this forces a new resource to be created.
        /// </summary>
        [Input("hostname")]
        public Input<string>? Hostname { get; set; }

        /// <summary>
        /// The server-assigned unique identifier of this instance.
        /// </summary>
        [Input("instanceId")]
        public Input<string>? InstanceId { get; set; }

        /// <summary>
        /// The unique fingerprint of the labels.
        /// </summary>
        [Input("labelFingerprint")]
        public Input<string>? LabelFingerprint { get; set; }

        [Input("labels")]
        private InputMap<string>? _labels;

        /// <summary>
        /// A set of key/value label pairs assigned to the instance.
        /// </summary>
        public InputMap<string> Labels
        {
            get => _labels ?? (_labels = new InputMap<string>());
            set => _labels = value;
        }

        /// <summary>
        /// The machine type to create.
        /// </summary>
        [Input("machineType")]
        public Input<string>? MachineType { get; set; }

        [Input("metadata")]
        private InputMap<string>? _metadata;

        /// <summary>
        /// Metadata key/value pairs made available within the instance.
        /// </summary>
        public InputMap<string> Metadata
        {
            get => _metadata ?? (_metadata = new InputMap<string>());
            set => _metadata = value;
        }

        /// <summary>
        /// The unique fingerprint of the metadata.
        /// </summary>
        [Input("metadataFingerprint")]
        public Input<string>? MetadataFingerprint { get; set; }

        /// <summary>
        /// Metadata startup scripts made available within the instance.
        /// </summary>
        [Input("metadataStartupScript")]
        public Input<string>? MetadataStartupScript { get; set; }

        /// <summary>
        /// The minimum CPU platform specified for the VM instance.
        /// </summary>
        [Input("minCpuPlatform")]
        public Input<string>? MinCpuPlatform { get; set; }

        /// <summary>
        /// A unique name for the resource, required by GCE.
        /// Changing this forces a new resource to be created.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        [Input("networkInterfaces")]
        private InputList<Inputs.InstanceFromMachineImageNetworkInterfaceGetArgs>? _networkInterfaces;

        /// <summary>
        /// The networks attached to the instance.
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageNetworkInterfaceGetArgs> NetworkInterfaces
        {
            get => _networkInterfaces ?? (_networkInterfaces = new InputList<Inputs.InstanceFromMachineImageNetworkInterfaceGetArgs>());
            set => _networkInterfaces = value;
        }

        /// <summary>
        /// The ID of the project in which the resource belongs. If self_link is provided, this value is ignored. If neither
        /// self_link nor project are provided, the provider project is used.
        /// </summary>
        [Input("project")]
        public Input<string>? Project { get; set; }

        /// <summary>
        /// A list of short names or self_links of resource policies to attach to the instance. Modifying this list will cause the
        /// instance to recreate. Currently a max of 1 resource policy is supported.
        /// </summary>
        [Input("resourcePolicies")]
        public Input<string>? ResourcePolicies { get; set; }

        /// <summary>
        /// The scheduling strategy being used by the instance.
        /// </summary>
        [Input("scheduling")]
        public Input<Inputs.InstanceFromMachineImageSchedulingGetArgs>? Scheduling { get; set; }

        [Input("scratchDisks")]
        private InputList<Inputs.InstanceFromMachineImageScratchDiskGetArgs>? _scratchDisks;

        /// <summary>
        /// The scratch disks attached to the instance.
        /// </summary>
        public InputList<Inputs.InstanceFromMachineImageScratchDiskGetArgs> ScratchDisks
        {
            get => _scratchDisks ?? (_scratchDisks = new InputList<Inputs.InstanceFromMachineImageScratchDiskGetArgs>());
            set => _scratchDisks = value;
        }

        /// <summary>
        /// The URI of the created resource.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// The service account to attach to the instance.
        /// </summary>
        [Input("serviceAccount")]
        public Input<Inputs.InstanceFromMachineImageServiceAccountGetArgs>? ServiceAccount { get; set; }

        /// <summary>
        /// The shielded vm config being used by the instance.
        /// </summary>
        [Input("shieldedInstanceConfig")]
        public Input<Inputs.InstanceFromMachineImageShieldedInstanceConfigGetArgs>? ShieldedInstanceConfig { get; set; }

        /// <summary>
        /// Name or self link of a machine
        /// image to create the instance based on.
        /// </summary>
        [Input("sourceMachineImage")]
        public Input<string>? SourceMachineImage { get; set; }

        [Input("tags")]
        private InputList<string>? _tags;

        /// <summary>
        /// The list of tags attached to the instance.
        /// </summary>
        public InputList<string> Tags
        {
            get => _tags ?? (_tags = new InputList<string>());
            set => _tags = value;
        }

        /// <summary>
        /// The unique fingerprint of the tags.
        /// </summary>
        [Input("tagsFingerprint")]
        public Input<string>? TagsFingerprint { get; set; }

        /// <summary>
        /// The zone that the machine should be created in. If not
        /// set, the provider zone is used.
        /// </summary>
        [Input("zone")]
        public Input<string>? Zone { get; set; }

        public InstanceFromMachineImageState()
        {
        }
    }
}
