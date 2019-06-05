// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Creates a group of dissimilar Compute Engine virtual machine instances.
 * For more information, see [the official documentation](https://cloud.google.com/compute/docs/instance-groups/#unmanaged_instance_groups)
 * and [API](https://cloud.google.com/compute/docs/reference/latest/instanceGroups)
 * 
 * > Recreating an instance group that's in use by another resource will give a
 * `resourceInUseByAnotherResource` error. You can avoid this error with a
 * Terraform `lifecycle` block as outlined in the example below.
 * 
 * ## Example Usage - Empty instance group
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const test = new gcp.compute.InstanceGroup("test", {
 *     description: "Terraform test instance group",
 *     network: google_compute_network_default.selfLink,
 *     zone: "us-central1-a",
 * });
 * ```
 * 
 * ### Example Usage - With instances and named ports
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const webservers = new gcp.compute.InstanceGroup("webservers", {
 *     description: "Terraform test instance group",
 *     instances: [
 *         google_compute_instance_test.selfLink,
 *         google_compute_instance_test2.selfLink,
 *     ],
 *     namedPorts: [
 *         {
 *             name: "http",
 *             port: 8080,
 *         },
 *         {
 *             name: "https",
 *             port: 8443,
 *         },
 *     ],
 *     zone: "us-central1-a",
 * });
 * ```
 * 
 * ### Example Usage - Recreating an instance group in use
 * Recreating an instance group that's in use by another resource will give a
 * `resourceInUseByAnotherResource` error. Use `lifecycle.create_before_destroy`
 * as shown in this example to avoid this type of error.
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const debianImage = pulumi.output(gcp.compute.getImage({
 *     family: "debian-9",
 *     project: "debian-cloud",
 * }));
 * const stagingHealth = new gcp.compute.HttpsHealthCheck("staging_health", {
 *     requestPath: "/health_check",
 * });
 * const stagingVm = new gcp.compute.Instance("staging_vm", {
 *     bootDisk: {
 *         initializeParams: {
 *             image: debianImage.selfLink,
 *         },
 *     },
 *     machineType: "n1-standard-1",
 *     networkInterfaces: [{
 *         network: "default",
 *     }],
 *     zone: "us-central1-c",
 * });
 * const stagingGroup = new gcp.compute.InstanceGroup("staging_group", {
 *     instances: [stagingVm.selfLink],
 *     namedPorts: [
 *         {
 *             name: "http",
 *             port: 8080,
 *         },
 *         {
 *             name: "https",
 *             port: 8443,
 *         },
 *     ],
 *     zone: "us-central1-c",
 * });
 * const stagingService = new gcp.compute.BackendService("staging_service", {
 *     backends: [{
 *         group: stagingGroup.selfLink,
 *     }],
 *     healthChecks: stagingHealth.selfLink,
 *     portName: "https",
 *     protocol: "HTTPS",
 * });
 * ```
 */
export class InstanceGroup extends pulumi.CustomResource {
    /**
     * Get an existing InstanceGroup resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: InstanceGroupState, opts?: pulumi.CustomResourceOptions): InstanceGroup {
        return new InstanceGroup(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/instanceGroup:InstanceGroup';

    /**
     * Returns true if the given object is an instance of InstanceGroup.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is InstanceGroup {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === InstanceGroup.__pulumiType;
    }

    /**
     * An optional textual description of the instance
     * group.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * List of instances in the group. They should be given
     * as self_link URLs. When adding instances they must all be in the same
     * network and zone as the instance group.
     */
    public readonly instances!: pulumi.Output<string[]>;
    /**
     * The name of the instance group. Must be 1-63
     * characters long and comply with
     * [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Supported characters
     * include lowercase letters, numbers, and hyphens.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The named port configuration. See the section below
     * for details on configuration.
     */
    public readonly namedPorts!: pulumi.Output<{ name: string, port: number }[] | undefined>;
    /**
     * The URL of the network the instance group is in. If
     * this is different from the network where the instances are in, the creation
     * fails. Defaults to the network where the instances are in (if neither
     * `network` nor `instances` is specified, this field will be blank).
     */
    public readonly network!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * The number of instances in the group.
     */
    public /*out*/ readonly size!: pulumi.Output<number>;
    /**
     * The zone that this instance group should be created in.
     */
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a InstanceGroup resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: InstanceGroupArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: InstanceGroupArgs | InstanceGroupState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as InstanceGroupState | undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["instances"] = state ? state.instances : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["namedPorts"] = state ? state.namedPorts : undefined;
            inputs["network"] = state ? state.network : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["size"] = state ? state.size : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as InstanceGroupArgs | undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["instances"] = args ? args.instances : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["namedPorts"] = args ? args.namedPorts : undefined;
            inputs["network"] = args ? args.network : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["selfLink"] = undefined /*out*/;
            inputs["size"] = undefined /*out*/;
        }
        super(InstanceGroup.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering InstanceGroup resources.
 */
export interface InstanceGroupState {
    /**
     * An optional textual description of the instance
     * group.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * List of instances in the group. They should be given
     * as self_link URLs. When adding instances they must all be in the same
     * network and zone as the instance group.
     */
    readonly instances?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the instance group. Must be 1-63
     * characters long and comply with
     * [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Supported characters
     * include lowercase letters, numbers, and hyphens.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The named port configuration. See the section below
     * for details on configuration.
     */
    readonly namedPorts?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, port: pulumi.Input<number> }>[]>;
    /**
     * The URL of the network the instance group is in. If
     * this is different from the network where the instances are in, the creation
     * fails. Defaults to the network where the instances are in (if neither
     * `network` nor `instances` is specified, this field will be blank).
     */
    readonly network?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    /**
     * The number of instances in the group.
     */
    readonly size?: pulumi.Input<number>;
    /**
     * The zone that this instance group should be created in.
     */
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a InstanceGroup resource.
 */
export interface InstanceGroupArgs {
    /**
     * An optional textual description of the instance
     * group.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * List of instances in the group. They should be given
     * as self_link URLs. When adding instances they must all be in the same
     * network and zone as the instance group.
     */
    readonly instances?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * The name of the instance group. Must be 1-63
     * characters long and comply with
     * [RFC1035](https://www.ietf.org/rfc/rfc1035.txt). Supported characters
     * include lowercase letters, numbers, and hyphens.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The named port configuration. See the section below
     * for details on configuration.
     */
    readonly namedPorts?: pulumi.Input<pulumi.Input<{ name: pulumi.Input<string>, port: pulumi.Input<number> }>[]>;
    /**
     * The URL of the network the instance group is in. If
     * this is different from the network where the instances are in, the creation
     * fails. Defaults to the network where the instances are in (if neither
     * `network` nor `instances` is specified, this field will be blank).
     */
    readonly network?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The zone that this instance group should be created in.
     */
    readonly zone?: pulumi.Input<string>;
}
