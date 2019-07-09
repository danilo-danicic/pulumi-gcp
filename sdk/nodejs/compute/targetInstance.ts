// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Represents a TargetInstance resource which defines an endpoint instance
 * that terminates traffic of certain protocols. In particular, they are used
 * in Protocol Forwarding, where forwarding rules can send packets to a
 * non-NAT’ed target instance. Each target instance contains a single
 * virtual machine instance that receives and handles traffic from the
 * corresponding forwarding rules.
 * 
 * 
 * To get more information about TargetInstance, see:
 * 
 * * [API documentation](https://cloud.google.com/compute/docs/reference/v1/targetInstances)
 * * How-to Guides
 *     * [Using Protocol Forwarding](https://cloud.google.com/compute/docs/protocol-forwarding)
 * 
 * ## Example Usage - Target Instance Basic
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const vmimage = pulumi.output(gcp.compute.getImage({
 *     family: "debian-9",
 *     project: "debian-cloud",
 * }));
 * const target_vm = new gcp.compute.Instance("target-vm", {
 *     bootDisk: {
 *         initializeParams: {
 *             image: vmimage.selfLink,
 *         },
 *     },
 *     machineType: "n1-standard-1",
 *     networkInterfaces: [{
 *         network: "default",
 *     }],
 *     zone: "us-central1-a",
 * });
 * const defaultTargetInstance = new gcp.compute.TargetInstance("default", {
 *     instance: target_vm.selfLink,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_target_instance.html.markdown.
 */
export class TargetInstance extends pulumi.CustomResource {
    /**
     * Get an existing TargetInstance resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: TargetInstanceState, opts?: pulumi.CustomResourceOptions): TargetInstance {
        return new TargetInstance(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/targetInstance:TargetInstance';

    /**
     * Returns true if the given object is an instance of TargetInstance.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is TargetInstance {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === TargetInstance.__pulumiType;
    }

    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly instance!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly natPolicy!: pulumi.Output<string | undefined>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    public readonly zone!: pulumi.Output<string>;

    /**
     * Create a TargetInstance resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: TargetInstanceArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: TargetInstanceArgs | TargetInstanceState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as TargetInstanceState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["instance"] = state ? state.instance : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["natPolicy"] = state ? state.natPolicy : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["zone"] = state ? state.zone : undefined;
        } else {
            const args = argsOrState as TargetInstanceArgs | undefined;
            if (!args || args.instance === undefined) {
                throw new Error("Missing required property 'instance'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["instance"] = args ? args.instance : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["natPolicy"] = args ? args.natPolicy : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["zone"] = args ? args.zone : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
        }
        super(TargetInstance.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering TargetInstance resources.
 */
export interface TargetInstanceState {
    readonly creationTimestamp?: pulumi.Input<string>;
    readonly description?: pulumi.Input<string>;
    readonly instance?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly natPolicy?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    readonly zone?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a TargetInstance resource.
 */
export interface TargetInstanceArgs {
    readonly description?: pulumi.Input<string>;
    readonly instance: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly natPolicy?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly zone?: pulumi.Input<string>;
}
