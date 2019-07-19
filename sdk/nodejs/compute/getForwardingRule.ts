// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Get a forwarding rule within GCE from its name.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as gcp from "@pulumi/gcp";
 * 
 * const my_forwarding_rule = pulumi.output(gcp.compute.getForwardingRule({
 *     name: "forwarding-rule-us-east1",
 * }));
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_forwarding_rule.html.markdown.
 */
export function getForwardingRule(args: GetForwardingRuleArgs, opts?: pulumi.InvokeOptions): Promise<GetForwardingRuleResult> & GetForwardingRuleResult {
    const promise: Promise<GetForwardingRuleResult> = pulumi.runtime.invoke("gcp:compute/getForwardingRule:getForwardingRule", {
        "name": args.name,
        "project": args.project,
        "region": args.region,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getForwardingRule.
 */
export interface GetForwardingRuleArgs {
    /**
     * The name of the forwarding rule.
     */
    readonly name: string;
    /**
     * The project in which the resource belongs. If it
     * is not provided, the provider project is used.
     */
    readonly project?: string;
    /**
     * The region in which the resource belongs. If it
     * is not provided, the project region is used.
     */
    readonly region?: string;
}

/**
 * A collection of values returned by getForwardingRule.
 */
export interface GetForwardingRuleResult {
    /**
     * Backend service, if this forwarding rule has one.
     */
    readonly backendService: string;
    /**
     * Description of this forwarding rule.
     */
    readonly description: string;
    /**
     * IP address of this forwarding rule.
     */
    readonly ipAddress: string;
    /**
     * IP protocol of this forwarding rule.
     */
    readonly ipProtocol: string;
    /**
     * Type of load balancing of this forwarding rule.
     */
    readonly loadBalancingScheme: string;
    readonly name: string;
    /**
     * Network of this forwarding rule.
     */
    readonly network: string;
    /**
     * Port range, if this forwarding rule has one.
     */
    readonly portRange: string;
    /**
     * List of ports to use for internal load balancing, if this forwarding rule has any.
     */
    readonly ports: string[];
    readonly project: string;
    /**
     * Region of this forwarding rule.
     */
    readonly region: string;
    /**
     * The URI of the resource.
     */
    readonly selfLink: string;
    /**
     * Subnetwork of this forwarding rule.
     */
    readonly subnetwork: string;
    /**
     * URL of the target pool, if this forwarding rule has one.
     */
    readonly target: string;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
