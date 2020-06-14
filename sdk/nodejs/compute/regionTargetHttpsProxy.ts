// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Represents a RegionTargetHttpsProxy resource, which is used by one or more
 * forwarding rules to route incoming HTTPS requests to a URL map.
 *
 * To get more information about RegionTargetHttpsProxy, see:
 *
 * * [API documentation](https://cloud.google.com/compute/docs/reference/rest/v1/regionTargetHttpsProxies)
 * * How-to Guides
 *     * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/target-proxies)
 *
 * ## Example Usage
 *
 * ### Region Target Https Proxy Basic
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * import * from "fs";
 *
 * const defaultRegionSslCertificate = new gcp.compute.RegionSslCertificate("defaultRegionSslCertificate", {
 *     region: "us-central1",
 *     privateKey: fs.readFileSync("path/to/private.key"),
 *     certificate: fs.readFileSync("path/to/certificate.crt"),
 * });
 * const defaultRegionHealthCheck = new gcp.compute.RegionHealthCheck("defaultRegionHealthCheck", {
 *     region: "us-central1",
 *     http_health_check: {
 *         port: 80,
 *     },
 * });
 * const defaultRegionBackendService = new gcp.compute.RegionBackendService("defaultRegionBackendService", {
 *     region: "us-central1",
 *     protocol: "HTTP",
 *     timeoutSec: 10,
 *     healthChecks: [defaultRegionHealthCheck.id],
 * });
 * const defaultRegionUrlMap = new gcp.compute.RegionUrlMap("defaultRegionUrlMap", {
 *     region: "us-central1",
 *     description: "a description",
 *     defaultService: defaultRegionBackendService.id,
 *     host_rule: [{
 *         hosts: ["mysite.com"],
 *         pathMatcher: "allpaths",
 *     }],
 *     path_matcher: [{
 *         name: "allpaths",
 *         defaultService: defaultRegionBackendService.id,
 *         path_rule: [{
 *             paths: ["/*"],
 *             service: defaultRegionBackendService.id,
 *         }],
 *     }],
 * });
 * const defaultRegionTargetHttpsProxy = new gcp.compute.RegionTargetHttpsProxy("defaultRegionTargetHttpsProxy", {
 *     region: "us-central1",
 *     urlMap: defaultRegionUrlMap.id,
 *     sslCertificates: [defaultRegionSslCertificate.id],
 * });
 * ```
 */
export class RegionTargetHttpsProxy extends pulumi.CustomResource {
    /**
     * Get an existing RegionTargetHttpsProxy resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RegionTargetHttpsProxyState, opts?: pulumi.CustomResourceOptions): RegionTargetHttpsProxy {
        return new RegionTargetHttpsProxy(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'gcp:compute/regionTargetHttpsProxy:RegionTargetHttpsProxy';

    /**
     * Returns true if the given object is an instance of RegionTargetHttpsProxy.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RegionTargetHttpsProxy {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RegionTargetHttpsProxy.__pulumiType;
    }

    /**
     * Creation timestamp in RFC3339 text format.
     */
    public /*out*/ readonly creationTimestamp!: pulumi.Output<string>;
    /**
     * An optional description of this resource.
     */
    public readonly description!: pulumi.Output<string | undefined>;
    /**
     * Name of the resource. Provided by the client when the resource is
     * created. The name must be 1-63 characters long, and comply with
     * RFC1035. Specifically, the name must be 1-63 characters long and match
     * the regular expression `a-z?` which means the
     * first character must be a lowercase letter, and all following
     * characters must be a dash, lowercase letter, or digit, except the last
     * character, which cannot be a dash.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    public readonly project!: pulumi.Output<string>;
    /**
     * The unique identifier for the resource.
     */
    public /*out*/ readonly proxyId!: pulumi.Output<number>;
    /**
     * The Region in which the created target https proxy should reside.
     * If it is not provided, the provider region is used.
     */
    public readonly region!: pulumi.Output<string>;
    /**
     * The URI of the created resource.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * A list of RegionSslCertificate resources that are used to authenticate
     * connections between users and the load balancer. Currently, exactly
     * one SSL certificate must be specified.
     */
    public readonly sslCertificates!: pulumi.Output<string[]>;
    /**
     * A reference to the RegionUrlMap resource that defines the mapping from URL
     * to the RegionBackendService.
     */
    public readonly urlMap!: pulumi.Output<string>;

    /**
     * Create a RegionTargetHttpsProxy resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RegionTargetHttpsProxyArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RegionTargetHttpsProxyArgs | RegionTargetHttpsProxyState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RegionTargetHttpsProxyState | undefined;
            inputs["creationTimestamp"] = state ? state.creationTimestamp : undefined;
            inputs["description"] = state ? state.description : undefined;
            inputs["name"] = state ? state.name : undefined;
            inputs["project"] = state ? state.project : undefined;
            inputs["proxyId"] = state ? state.proxyId : undefined;
            inputs["region"] = state ? state.region : undefined;
            inputs["selfLink"] = state ? state.selfLink : undefined;
            inputs["sslCertificates"] = state ? state.sslCertificates : undefined;
            inputs["urlMap"] = state ? state.urlMap : undefined;
        } else {
            const args = argsOrState as RegionTargetHttpsProxyArgs | undefined;
            if (!args || args.sslCertificates === undefined) {
                throw new Error("Missing required property 'sslCertificates'");
            }
            if (!args || args.urlMap === undefined) {
                throw new Error("Missing required property 'urlMap'");
            }
            inputs["description"] = args ? args.description : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["project"] = args ? args.project : undefined;
            inputs["region"] = args ? args.region : undefined;
            inputs["sslCertificates"] = args ? args.sslCertificates : undefined;
            inputs["urlMap"] = args ? args.urlMap : undefined;
            inputs["creationTimestamp"] = undefined /*out*/;
            inputs["proxyId"] = undefined /*out*/;
            inputs["selfLink"] = undefined /*out*/;
        }
        if (!opts) {
            opts = {}
        }

        if (!opts.version) {
            opts.version = utilities.getVersion();
        }
        super(RegionTargetHttpsProxy.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RegionTargetHttpsProxy resources.
 */
export interface RegionTargetHttpsProxyState {
    /**
     * Creation timestamp in RFC3339 text format.
     */
    readonly creationTimestamp?: pulumi.Input<string>;
    /**
     * An optional description of this resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Name of the resource. Provided by the client when the resource is
     * created. The name must be 1-63 characters long, and comply with
     * RFC1035. Specifically, the name must be 1-63 characters long and match
     * the regular expression `a-z?` which means the
     * first character must be a lowercase letter, and all following
     * characters must be a dash, lowercase letter, or digit, except the last
     * character, which cannot be a dash.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The unique identifier for the resource.
     */
    readonly proxyId?: pulumi.Input<number>;
    /**
     * The Region in which the created target https proxy should reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * The URI of the created resource.
     */
    readonly selfLink?: pulumi.Input<string>;
    /**
     * A list of RegionSslCertificate resources that are used to authenticate
     * connections between users and the load balancer. Currently, exactly
     * one SSL certificate must be specified.
     */
    readonly sslCertificates?: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A reference to the RegionUrlMap resource that defines the mapping from URL
     * to the RegionBackendService.
     */
    readonly urlMap?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RegionTargetHttpsProxy resource.
 */
export interface RegionTargetHttpsProxyArgs {
    /**
     * An optional description of this resource.
     */
    readonly description?: pulumi.Input<string>;
    /**
     * Name of the resource. Provided by the client when the resource is
     * created. The name must be 1-63 characters long, and comply with
     * RFC1035. Specifically, the name must be 1-63 characters long and match
     * the regular expression `a-z?` which means the
     * first character must be a lowercase letter, and all following
     * characters must be a dash, lowercase letter, or digit, except the last
     * character, which cannot be a dash.
     */
    readonly name?: pulumi.Input<string>;
    /**
     * The ID of the project in which the resource belongs.
     * If it is not provided, the provider project is used.
     */
    readonly project?: pulumi.Input<string>;
    /**
     * The Region in which the created target https proxy should reside.
     * If it is not provided, the provider region is used.
     */
    readonly region?: pulumi.Input<string>;
    /**
     * A list of RegionSslCertificate resources that are used to authenticate
     * connections between users and the load balancer. Currently, exactly
     * one SSL certificate must be specified.
     */
    readonly sslCertificates: pulumi.Input<pulumi.Input<string>[]>;
    /**
     * A reference to the RegionUrlMap resource that defines the mapping from URL
     * to the RegionBackendService.
     */
    readonly urlMap: pulumi.Input<string>;
}
