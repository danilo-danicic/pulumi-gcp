// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Represents a VPN gateway running in GCP. This virtual device is managed
 * by Google, but used only by you.
 * 
 * 
 * To get more information about VpnGateway, see:
 * 
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/targetVpnGateways)
 * 
 * ## Example Usage - Target Vpn Gateway Basic
 * 
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const vpnStaticIp = new gcp.compute.Address("vpn_static_ip", {});
 * const network1 = new gcp.compute.Network("network1", {});
 * const targetGateway = new gcp.compute.VPNGateway("target_gateway", {
 *     network: network1.selfLink,
 * });
 * const frEsp = new gcp.compute.ForwardingRule("fr_esp", {
 *     ipAddress: vpnStaticIp.address,
 *     ipProtocol: "ESP",
 *     target: targetGateway.selfLink,
 * });
 * const frUdp4500 = new gcp.compute.ForwardingRule("fr_udp4500", {
 *     ipAddress: vpnStaticIp.address,
 *     ipProtocol: "UDP",
 *     portRange: "4500",
 *     target: targetGateway.selfLink,
 * });
 * const frUdp500 = new gcp.compute.ForwardingRule("fr_udp500", {
 *     ipAddress: vpnStaticIp.address,
 *     ipProtocol: "UDP",
 *     portRange: "500",
 *     target: targetGateway.selfLink,
 * });
 * const tunnel1 = new gcp.compute.VPNTunnel("tunnel1", {
 *     peerIp: "15.0.0.120",
 *     sharedSecret: "a secret message",
 *     targetVpnGateway: targetGateway.selfLink,
 * }, {dependsOn: [frEsp, frUdp4500, frUdp500]});
 * const route1 = new gcp.compute.Route("route1", {
 *     destRange: "15.0.0.0/24",
 *     network: network1.name,
 *     nextHopVpnTunnel: tunnel1.selfLink,
 *     priority: 1000,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/compute_vpn_gateway.html.markdown.
 */
export class VPNGateway extends pulumi.CustomResource {
    /**
     * Get an existing VPNGateway resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VPNGatewayState, opts?: pulumi.CustomResourceOptions): VPNGateway {
        return new VPNGateway(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/vPNGateway:VPNGateway';

    /**
     * Returns true if the given object is an instance of VPNGateway.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VPNGateway {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VPNGateway.__pulumiType;
    }

    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly network!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    public readonly region!: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;

    /**
     * Create a VPNGateway resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VPNGatewayArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VPNGatewayArgs | VPNGatewayState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as VPNGatewayState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["network"] = state ? state.network : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
        } else {
            const args = argsOrState as VPNGatewayArgs | undefined;
            if (!args || args.network === undefined) {
                throw new Error("Missing required property 'network'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["network"] = args ? args.network : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
        }
        super(VPNGateway.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VPNGateway resources.
 */
export interface VPNGatewayState {
    readonly creationTimestamp?: pulumi.Input<string>;
    readonly description?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly network?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VPNGateway resource.
 */
export interface VPNGatewayArgs {
    readonly description?: pulumi.Input<string>;
    readonly name?: pulumi.Input<string>;
    readonly network: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    readonly region?: pulumi.Input<string>;
}
