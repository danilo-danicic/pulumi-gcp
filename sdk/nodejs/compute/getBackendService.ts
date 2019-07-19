// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Provide access to a Backend Service's attribute. For more information
 * see [the official documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
 * and the [API](https://cloud.google.com/compute/docs/reference/latest/backendServices).
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/d/compute_backend_service.html.markdown.
 */
export function getBackendService(args: GetBackendServiceArgs, opts?: pulumi.InvokeOptions): Promise<GetBackendServiceResult> & GetBackendServiceResult {
    const promise: Promise<GetBackendServiceResult> = pulumi.runtime.invoke("gcp:compute/getBackendService:getBackendService", {
        "name": args.name,
        "project": args.project,
    }, opts);

    return pulumi.utils.liftProperties(promise, opts);
}

/**
 * A collection of arguments for invoking getBackendService.
 */
export interface GetBackendServiceArgs {
    /**
     * The name of the Backend Service.
     */
    readonly name: string;
    /**
     * The project in which the resource belongs. If it is not provided, the provider project is used.
     */
    readonly project?: string;
}

/**
 * A collection of values returned by getBackendService.
 */
export interface GetBackendServiceResult {
    readonly affinityCookieTtlSec: number;
    /**
     * The set of backends that serve this Backend Service.
     */
    readonly backends: { balancingMode: string, capacityScaler: number, description: string, group: string, maxConnections: number, maxConnectionsPerEndpoint: number, maxConnectionsPerInstance: number, maxRate: number, maxRatePerEndpoint: number, maxRatePerInstance: number, maxUtilization: number }[];
    readonly cdnPolicies: { cacheKeyPolicies: { includeHost: boolean, includeProtocol: boolean, includeQueryString: boolean, queryStringBlacklists: string[], queryStringWhitelists: string[] }[], signedUrlCacheMaxAgeSec: number }[];
    /**
     * Time for which instance will be drained (not accept new connections, but still work to finish started ones).
     */
    readonly connectionDrainingTimeoutSec: number;
    readonly creationTimestamp: string;
    readonly customRequestHeaders: string[];
    /**
     * Textual description for the Backend Service.
     */
    readonly description: string;
    /**
     * Whether or not Cloud CDN is enabled on the Backend Service.
     */
    readonly enableCdn: boolean;
    /**
     * The fingerprint of the Backend Service.
     */
    readonly fingerprint: string;
    /**
     * The set of HTTP/HTTPS health checks used by the Backend Service.
     */
    readonly healthChecks: string[];
    readonly iaps: { oauth2ClientId: string, oauth2ClientSecret: string, oauth2ClientSecretSha256: string }[];
    readonly loadBalancingScheme: string;
    readonly name: string;
    /**
     * The name of a service that has been added to an instance group in this backend.
     */
    readonly portName: string;
    readonly project?: string;
    /**
     * The protocol for incoming requests.
     */
    readonly protocol: string;
    readonly securityPolicy: string;
    /**
     * The URI of the Backend Service.
     */
    readonly selfLink: string;
    /**
     * The Backend Service session stickyness configuration.
     */
    readonly sessionAffinity: string;
    /**
     * The number of seconds to wait for a backend to respond to a request before considering the request failed.
     */
    readonly timeoutSec: number;
    /**
     * id is the provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
}
