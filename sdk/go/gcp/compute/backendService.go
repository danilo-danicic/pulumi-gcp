// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package compute

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// A Backend Service defines a group of virtual machines that will serve
// traffic for load balancing. This resource is a global backend service,
// appropriate for external load balancing or self-managed internal load balancing.
// For managed internal load balancing, use a regional backend service instead.
//
// Currently self-managed internal load balancing is only available in beta.
//
// To get more information about BackendService, see:
//
// * [API documentation](https://cloud.google.com/compute/docs/reference/v1/backendServices)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/compute/docs/load-balancing/http/backend-service)
//
// ## Example Usage
type BackendService struct {
	pulumi.CustomResourceState

	// Lifetime of cookies in seconds if sessionAffinity is
	// GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
	// only until the end of the browser session (or equivalent). The
	// maximum allowed value for TTL is one day.
	// When the load balancing scheme is INTERNAL, this field is not used.
	AffinityCookieTtlSec pulumi.IntPtrOutput `pulumi:"affinityCookieTtlSec"`
	// The set of backends that serve this BackendService.
	// Structure is documented below.
	Backends BackendServiceBackendArrayOutput `pulumi:"backends"`
	// Cloud CDN configuration for this BackendService.
	// Structure is documented below.
	CdnPolicy BackendServiceCdnPolicyOutput `pulumi:"cdnPolicy"`
	// Settings controlling the volume of connections to a backend service. This field
	// is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	CircuitBreakers BackendServiceCircuitBreakersPtrOutput `pulumi:"circuitBreakers"`
	// Time for which instance will be drained (not accept new
	// connections, but still work to finish started).
	ConnectionDrainingTimeoutSec pulumi.IntPtrOutput `pulumi:"connectionDrainingTimeoutSec"`
	// Consistent Hash-based load balancing can be used to provide soft session
	// affinity based on HTTP headers, cookies or other properties. This load balancing
	// policy is applicable only for HTTP connections. The affinity to a particular
	// destination host will be lost when one or more hosts are added/removed from the
	// destination service. This field specifies parameters that control consistent
	// hashing. This field only applies if the loadBalancingScheme is set to
	// INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
	// set to MAGLEV or RING_HASH.
	// Structure is documented below.
	ConsistentHash BackendServiceConsistentHashPtrOutput `pulumi:"consistentHash"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringOutput `pulumi:"creationTimestamp"`
	// Headers that the HTTP/S load balancer should add to proxied
	// requests.
	CustomRequestHeaders pulumi.StringArrayOutput `pulumi:"customRequestHeaders"`
	// An optional description of this resource.
	// Provide this property when you create the resource.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// If true, enable Cloud CDN for this BackendService.
	EnableCdn pulumi.BoolPtrOutput `pulumi:"enableCdn"`
	// Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
	Fingerprint pulumi.StringOutput `pulumi:"fingerprint"`
	// The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
	// for health checking this BackendService. Currently at most one health
	// check can be specified.
	// A health check must be specified unless the backend service uses an internet
	// or serverless NEG as a backend.
	// For internal load balancing, a URL to a HealthCheck resource must be specified instead.
	HealthChecks pulumi.StringPtrOutput `pulumi:"healthChecks"`
	// Settings for enabling Cloud Identity Aware Proxy
	// Structure is documented below.
	Iap BackendServiceIapPtrOutput `pulumi:"iap"`
	// Indicates whether the backend service will be used with internal or
	// external load balancing. A backend service created for one type of
	// load balancing cannot be used with the other.
	// Default value is `EXTERNAL`.
	// Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
	LoadBalancingScheme pulumi.StringPtrOutput `pulumi:"loadBalancingScheme"`
	// The load balancing algorithm used within the scope of the locality.
	// The possible values are -
	// * ROUND_ROBIN - This is a simple policy in which each healthy backend
	//   is selected in round robin order.
	// * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
	//   hosts and picks the host which has fewer active requests.
	// * RING_HASH - The ring/modulo hash load balancer implements consistent
	//   hashing to backends. The algorithm has the property that the
	//   addition/removal of a host from a set of N hosts only affects
	//   1/N of the requests.
	// * RANDOM - The load balancer selects a random healthy host.
	// * ORIGINAL_DESTINATION - Backend host is selected based on the client
	//   connection metadata, i.e., connections are opened
	//   to the same address as the destination address of
	//   the incoming connection before the connection
	//   was redirected to the load balancer.
	// * MAGLEV - used as a drop in replacement for the ring hash load balancer.
	//   Maglev is not as stable as ring hash but has faster table lookup
	//   build times and host selection times. For more information about
	//   Maglev, refer to https://ai.google/research/pubs/pub44824
	//   This field is applicable only when the loadBalancingScheme is set to
	//   INTERNAL_SELF_MANAGED.
	//   Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
	LocalityLbPolicy pulumi.StringPtrOutput `pulumi:"localityLbPolicy"`
	// This field denotes the logging options for the load balancer traffic served by this backend service.
	// If logging is enabled, logs will be exported to Stackdriver.
	// Structure is documented below.
	LogConfig BackendServiceLogConfigOutput `pulumi:"logConfig"`
	// Name of the cookie.
	Name pulumi.StringOutput `pulumi:"name"`
	// Settings controlling eviction of unhealthy hosts from the load balancing pool.
	// This field is applicable only when the loadBalancingScheme is set
	// to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	OutlierDetection BackendServiceOutlierDetectionPtrOutput `pulumi:"outlierDetection"`
	// Name of backend port. The same name should appear in the instance
	// groups referenced by this service. Required when the load balancing
	// scheme is EXTERNAL.
	PortName pulumi.StringOutput `pulumi:"portName"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// The protocol this BackendService uses to communicate with backends.
	// The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
	// types and may result in errors if used with the GA API.
	// Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, `SSL`, and `GRPC`.
	Protocol pulumi.StringOutput `pulumi:"protocol"`
	// The security policy associated with this backend service.
	SecurityPolicy pulumi.StringPtrOutput `pulumi:"securityPolicy"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// Type of session affinity to use. The default is NONE. Session affinity is
	// not applicable if the protocol is UDP.
	// Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
	SessionAffinity pulumi.StringOutput `pulumi:"sessionAffinity"`
	// How many seconds to wait for the backend before considering it a
	// failed request. Default is 30 seconds. Valid range is [1, 86400].
	TimeoutSec pulumi.IntOutput `pulumi:"timeoutSec"`
}

// NewBackendService registers a new resource with the given unique name, arguments, and options.
func NewBackendService(ctx *pulumi.Context,
	name string, args *BackendServiceArgs, opts ...pulumi.ResourceOption) (*BackendService, error) {
	if args == nil {
		args = &BackendServiceArgs{}
	}
	var resource BackendService
	err := ctx.RegisterResource("gcp:compute/backendService:BackendService", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetBackendService gets an existing BackendService resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetBackendService(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *BackendServiceState, opts ...pulumi.ResourceOption) (*BackendService, error) {
	var resource BackendService
	err := ctx.ReadResource("gcp:compute/backendService:BackendService", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering BackendService resources.
type backendServiceState struct {
	// Lifetime of cookies in seconds if sessionAffinity is
	// GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
	// only until the end of the browser session (or equivalent). The
	// maximum allowed value for TTL is one day.
	// When the load balancing scheme is INTERNAL, this field is not used.
	AffinityCookieTtlSec *int `pulumi:"affinityCookieTtlSec"`
	// The set of backends that serve this BackendService.
	// Structure is documented below.
	Backends []BackendServiceBackend `pulumi:"backends"`
	// Cloud CDN configuration for this BackendService.
	// Structure is documented below.
	CdnPolicy *BackendServiceCdnPolicy `pulumi:"cdnPolicy"`
	// Settings controlling the volume of connections to a backend service. This field
	// is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	CircuitBreakers *BackendServiceCircuitBreakers `pulumi:"circuitBreakers"`
	// Time for which instance will be drained (not accept new
	// connections, but still work to finish started).
	ConnectionDrainingTimeoutSec *int `pulumi:"connectionDrainingTimeoutSec"`
	// Consistent Hash-based load balancing can be used to provide soft session
	// affinity based on HTTP headers, cookies or other properties. This load balancing
	// policy is applicable only for HTTP connections. The affinity to a particular
	// destination host will be lost when one or more hosts are added/removed from the
	// destination service. This field specifies parameters that control consistent
	// hashing. This field only applies if the loadBalancingScheme is set to
	// INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
	// set to MAGLEV or RING_HASH.
	// Structure is documented below.
	ConsistentHash *BackendServiceConsistentHash `pulumi:"consistentHash"`
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp *string `pulumi:"creationTimestamp"`
	// Headers that the HTTP/S load balancer should add to proxied
	// requests.
	CustomRequestHeaders []string `pulumi:"customRequestHeaders"`
	// An optional description of this resource.
	// Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// If true, enable Cloud CDN for this BackendService.
	EnableCdn *bool `pulumi:"enableCdn"`
	// Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
	Fingerprint *string `pulumi:"fingerprint"`
	// The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
	// for health checking this BackendService. Currently at most one health
	// check can be specified.
	// A health check must be specified unless the backend service uses an internet
	// or serverless NEG as a backend.
	// For internal load balancing, a URL to a HealthCheck resource must be specified instead.
	HealthChecks *string `pulumi:"healthChecks"`
	// Settings for enabling Cloud Identity Aware Proxy
	// Structure is documented below.
	Iap *BackendServiceIap `pulumi:"iap"`
	// Indicates whether the backend service will be used with internal or
	// external load balancing. A backend service created for one type of
	// load balancing cannot be used with the other.
	// Default value is `EXTERNAL`.
	// Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
	LoadBalancingScheme *string `pulumi:"loadBalancingScheme"`
	// The load balancing algorithm used within the scope of the locality.
	// The possible values are -
	// * ROUND_ROBIN - This is a simple policy in which each healthy backend
	//   is selected in round robin order.
	// * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
	//   hosts and picks the host which has fewer active requests.
	// * RING_HASH - The ring/modulo hash load balancer implements consistent
	//   hashing to backends. The algorithm has the property that the
	//   addition/removal of a host from a set of N hosts only affects
	//   1/N of the requests.
	// * RANDOM - The load balancer selects a random healthy host.
	// * ORIGINAL_DESTINATION - Backend host is selected based on the client
	//   connection metadata, i.e., connections are opened
	//   to the same address as the destination address of
	//   the incoming connection before the connection
	//   was redirected to the load balancer.
	// * MAGLEV - used as a drop in replacement for the ring hash load balancer.
	//   Maglev is not as stable as ring hash but has faster table lookup
	//   build times and host selection times. For more information about
	//   Maglev, refer to https://ai.google/research/pubs/pub44824
	//   This field is applicable only when the loadBalancingScheme is set to
	//   INTERNAL_SELF_MANAGED.
	//   Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
	LocalityLbPolicy *string `pulumi:"localityLbPolicy"`
	// This field denotes the logging options for the load balancer traffic served by this backend service.
	// If logging is enabled, logs will be exported to Stackdriver.
	// Structure is documented below.
	LogConfig *BackendServiceLogConfig `pulumi:"logConfig"`
	// Name of the cookie.
	Name *string `pulumi:"name"`
	// Settings controlling eviction of unhealthy hosts from the load balancing pool.
	// This field is applicable only when the loadBalancingScheme is set
	// to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	OutlierDetection *BackendServiceOutlierDetection `pulumi:"outlierDetection"`
	// Name of backend port. The same name should appear in the instance
	// groups referenced by this service. Required when the load balancing
	// scheme is EXTERNAL.
	PortName *string `pulumi:"portName"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The protocol this BackendService uses to communicate with backends.
	// The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
	// types and may result in errors if used with the GA API.
	// Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, `SSL`, and `GRPC`.
	Protocol *string `pulumi:"protocol"`
	// The security policy associated with this backend service.
	SecurityPolicy *string `pulumi:"securityPolicy"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// Type of session affinity to use. The default is NONE. Session affinity is
	// not applicable if the protocol is UDP.
	// Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
	SessionAffinity *string `pulumi:"sessionAffinity"`
	// How many seconds to wait for the backend before considering it a
	// failed request. Default is 30 seconds. Valid range is [1, 86400].
	TimeoutSec *int `pulumi:"timeoutSec"`
}

type BackendServiceState struct {
	// Lifetime of cookies in seconds if sessionAffinity is
	// GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
	// only until the end of the browser session (or equivalent). The
	// maximum allowed value for TTL is one day.
	// When the load balancing scheme is INTERNAL, this field is not used.
	AffinityCookieTtlSec pulumi.IntPtrInput
	// The set of backends that serve this BackendService.
	// Structure is documented below.
	Backends BackendServiceBackendArrayInput
	// Cloud CDN configuration for this BackendService.
	// Structure is documented below.
	CdnPolicy BackendServiceCdnPolicyPtrInput
	// Settings controlling the volume of connections to a backend service. This field
	// is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	CircuitBreakers BackendServiceCircuitBreakersPtrInput
	// Time for which instance will be drained (not accept new
	// connections, but still work to finish started).
	ConnectionDrainingTimeoutSec pulumi.IntPtrInput
	// Consistent Hash-based load balancing can be used to provide soft session
	// affinity based on HTTP headers, cookies or other properties. This load balancing
	// policy is applicable only for HTTP connections. The affinity to a particular
	// destination host will be lost when one or more hosts are added/removed from the
	// destination service. This field specifies parameters that control consistent
	// hashing. This field only applies if the loadBalancingScheme is set to
	// INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
	// set to MAGLEV or RING_HASH.
	// Structure is documented below.
	ConsistentHash BackendServiceConsistentHashPtrInput
	// Creation timestamp in RFC3339 text format.
	CreationTimestamp pulumi.StringPtrInput
	// Headers that the HTTP/S load balancer should add to proxied
	// requests.
	CustomRequestHeaders pulumi.StringArrayInput
	// An optional description of this resource.
	// Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// If true, enable Cloud CDN for this BackendService.
	EnableCdn pulumi.BoolPtrInput
	// Fingerprint of this resource. A hash of the contents stored in this object. This field is used in optimistic locking.
	Fingerprint pulumi.StringPtrInput
	// The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
	// for health checking this BackendService. Currently at most one health
	// check can be specified.
	// A health check must be specified unless the backend service uses an internet
	// or serverless NEG as a backend.
	// For internal load balancing, a URL to a HealthCheck resource must be specified instead.
	HealthChecks pulumi.StringPtrInput
	// Settings for enabling Cloud Identity Aware Proxy
	// Structure is documented below.
	Iap BackendServiceIapPtrInput
	// Indicates whether the backend service will be used with internal or
	// external load balancing. A backend service created for one type of
	// load balancing cannot be used with the other.
	// Default value is `EXTERNAL`.
	// Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
	LoadBalancingScheme pulumi.StringPtrInput
	// The load balancing algorithm used within the scope of the locality.
	// The possible values are -
	// * ROUND_ROBIN - This is a simple policy in which each healthy backend
	//   is selected in round robin order.
	// * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
	//   hosts and picks the host which has fewer active requests.
	// * RING_HASH - The ring/modulo hash load balancer implements consistent
	//   hashing to backends. The algorithm has the property that the
	//   addition/removal of a host from a set of N hosts only affects
	//   1/N of the requests.
	// * RANDOM - The load balancer selects a random healthy host.
	// * ORIGINAL_DESTINATION - Backend host is selected based on the client
	//   connection metadata, i.e., connections are opened
	//   to the same address as the destination address of
	//   the incoming connection before the connection
	//   was redirected to the load balancer.
	// * MAGLEV - used as a drop in replacement for the ring hash load balancer.
	//   Maglev is not as stable as ring hash but has faster table lookup
	//   build times and host selection times. For more information about
	//   Maglev, refer to https://ai.google/research/pubs/pub44824
	//   This field is applicable only when the loadBalancingScheme is set to
	//   INTERNAL_SELF_MANAGED.
	//   Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
	LocalityLbPolicy pulumi.StringPtrInput
	// This field denotes the logging options for the load balancer traffic served by this backend service.
	// If logging is enabled, logs will be exported to Stackdriver.
	// Structure is documented below.
	LogConfig BackendServiceLogConfigPtrInput
	// Name of the cookie.
	Name pulumi.StringPtrInput
	// Settings controlling eviction of unhealthy hosts from the load balancing pool.
	// This field is applicable only when the loadBalancingScheme is set
	// to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	OutlierDetection BackendServiceOutlierDetectionPtrInput
	// Name of backend port. The same name should appear in the instance
	// groups referenced by this service. Required when the load balancing
	// scheme is EXTERNAL.
	PortName pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The protocol this BackendService uses to communicate with backends.
	// The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
	// types and may result in errors if used with the GA API.
	// Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, `SSL`, and `GRPC`.
	Protocol pulumi.StringPtrInput
	// The security policy associated with this backend service.
	SecurityPolicy pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// Type of session affinity to use. The default is NONE. Session affinity is
	// not applicable if the protocol is UDP.
	// Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
	SessionAffinity pulumi.StringPtrInput
	// How many seconds to wait for the backend before considering it a
	// failed request. Default is 30 seconds. Valid range is [1, 86400].
	TimeoutSec pulumi.IntPtrInput
}

func (BackendServiceState) ElementType() reflect.Type {
	return reflect.TypeOf((*backendServiceState)(nil)).Elem()
}

type backendServiceArgs struct {
	// Lifetime of cookies in seconds if sessionAffinity is
	// GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
	// only until the end of the browser session (or equivalent). The
	// maximum allowed value for TTL is one day.
	// When the load balancing scheme is INTERNAL, this field is not used.
	AffinityCookieTtlSec *int `pulumi:"affinityCookieTtlSec"`
	// The set of backends that serve this BackendService.
	// Structure is documented below.
	Backends []BackendServiceBackend `pulumi:"backends"`
	// Cloud CDN configuration for this BackendService.
	// Structure is documented below.
	CdnPolicy *BackendServiceCdnPolicy `pulumi:"cdnPolicy"`
	// Settings controlling the volume of connections to a backend service. This field
	// is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	CircuitBreakers *BackendServiceCircuitBreakers `pulumi:"circuitBreakers"`
	// Time for which instance will be drained (not accept new
	// connections, but still work to finish started).
	ConnectionDrainingTimeoutSec *int `pulumi:"connectionDrainingTimeoutSec"`
	// Consistent Hash-based load balancing can be used to provide soft session
	// affinity based on HTTP headers, cookies or other properties. This load balancing
	// policy is applicable only for HTTP connections. The affinity to a particular
	// destination host will be lost when one or more hosts are added/removed from the
	// destination service. This field specifies parameters that control consistent
	// hashing. This field only applies if the loadBalancingScheme is set to
	// INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
	// set to MAGLEV or RING_HASH.
	// Structure is documented below.
	ConsistentHash *BackendServiceConsistentHash `pulumi:"consistentHash"`
	// Headers that the HTTP/S load balancer should add to proxied
	// requests.
	CustomRequestHeaders []string `pulumi:"customRequestHeaders"`
	// An optional description of this resource.
	// Provide this property when you create the resource.
	Description *string `pulumi:"description"`
	// If true, enable Cloud CDN for this BackendService.
	EnableCdn *bool `pulumi:"enableCdn"`
	// The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
	// for health checking this BackendService. Currently at most one health
	// check can be specified.
	// A health check must be specified unless the backend service uses an internet
	// or serverless NEG as a backend.
	// For internal load balancing, a URL to a HealthCheck resource must be specified instead.
	HealthChecks *string `pulumi:"healthChecks"`
	// Settings for enabling Cloud Identity Aware Proxy
	// Structure is documented below.
	Iap *BackendServiceIap `pulumi:"iap"`
	// Indicates whether the backend service will be used with internal or
	// external load balancing. A backend service created for one type of
	// load balancing cannot be used with the other.
	// Default value is `EXTERNAL`.
	// Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
	LoadBalancingScheme *string `pulumi:"loadBalancingScheme"`
	// The load balancing algorithm used within the scope of the locality.
	// The possible values are -
	// * ROUND_ROBIN - This is a simple policy in which each healthy backend
	//   is selected in round robin order.
	// * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
	//   hosts and picks the host which has fewer active requests.
	// * RING_HASH - The ring/modulo hash load balancer implements consistent
	//   hashing to backends. The algorithm has the property that the
	//   addition/removal of a host from a set of N hosts only affects
	//   1/N of the requests.
	// * RANDOM - The load balancer selects a random healthy host.
	// * ORIGINAL_DESTINATION - Backend host is selected based on the client
	//   connection metadata, i.e., connections are opened
	//   to the same address as the destination address of
	//   the incoming connection before the connection
	//   was redirected to the load balancer.
	// * MAGLEV - used as a drop in replacement for the ring hash load balancer.
	//   Maglev is not as stable as ring hash but has faster table lookup
	//   build times and host selection times. For more information about
	//   Maglev, refer to https://ai.google/research/pubs/pub44824
	//   This field is applicable only when the loadBalancingScheme is set to
	//   INTERNAL_SELF_MANAGED.
	//   Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
	LocalityLbPolicy *string `pulumi:"localityLbPolicy"`
	// This field denotes the logging options for the load balancer traffic served by this backend service.
	// If logging is enabled, logs will be exported to Stackdriver.
	// Structure is documented below.
	LogConfig *BackendServiceLogConfig `pulumi:"logConfig"`
	// Name of the cookie.
	Name *string `pulumi:"name"`
	// Settings controlling eviction of unhealthy hosts from the load balancing pool.
	// This field is applicable only when the loadBalancingScheme is set
	// to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	OutlierDetection *BackendServiceOutlierDetection `pulumi:"outlierDetection"`
	// Name of backend port. The same name should appear in the instance
	// groups referenced by this service. Required when the load balancing
	// scheme is EXTERNAL.
	PortName *string `pulumi:"portName"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// The protocol this BackendService uses to communicate with backends.
	// The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
	// types and may result in errors if used with the GA API.
	// Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, `SSL`, and `GRPC`.
	Protocol *string `pulumi:"protocol"`
	// The security policy associated with this backend service.
	SecurityPolicy *string `pulumi:"securityPolicy"`
	// Type of session affinity to use. The default is NONE. Session affinity is
	// not applicable if the protocol is UDP.
	// Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
	SessionAffinity *string `pulumi:"sessionAffinity"`
	// How many seconds to wait for the backend before considering it a
	// failed request. Default is 30 seconds. Valid range is [1, 86400].
	TimeoutSec *int `pulumi:"timeoutSec"`
}

// The set of arguments for constructing a BackendService resource.
type BackendServiceArgs struct {
	// Lifetime of cookies in seconds if sessionAffinity is
	// GENERATED_COOKIE. If set to 0, the cookie is non-persistent and lasts
	// only until the end of the browser session (or equivalent). The
	// maximum allowed value for TTL is one day.
	// When the load balancing scheme is INTERNAL, this field is not used.
	AffinityCookieTtlSec pulumi.IntPtrInput
	// The set of backends that serve this BackendService.
	// Structure is documented below.
	Backends BackendServiceBackendArrayInput
	// Cloud CDN configuration for this BackendService.
	// Structure is documented below.
	CdnPolicy BackendServiceCdnPolicyPtrInput
	// Settings controlling the volume of connections to a backend service. This field
	// is applicable only when the loadBalancingScheme is set to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	CircuitBreakers BackendServiceCircuitBreakersPtrInput
	// Time for which instance will be drained (not accept new
	// connections, but still work to finish started).
	ConnectionDrainingTimeoutSec pulumi.IntPtrInput
	// Consistent Hash-based load balancing can be used to provide soft session
	// affinity based on HTTP headers, cookies or other properties. This load balancing
	// policy is applicable only for HTTP connections. The affinity to a particular
	// destination host will be lost when one or more hosts are added/removed from the
	// destination service. This field specifies parameters that control consistent
	// hashing. This field only applies if the loadBalancingScheme is set to
	// INTERNAL_SELF_MANAGED. This field is only applicable when localityLbPolicy is
	// set to MAGLEV or RING_HASH.
	// Structure is documented below.
	ConsistentHash BackendServiceConsistentHashPtrInput
	// Headers that the HTTP/S load balancer should add to proxied
	// requests.
	CustomRequestHeaders pulumi.StringArrayInput
	// An optional description of this resource.
	// Provide this property when you create the resource.
	Description pulumi.StringPtrInput
	// If true, enable Cloud CDN for this BackendService.
	EnableCdn pulumi.BoolPtrInput
	// The set of URLs to the HttpHealthCheck or HttpsHealthCheck resource
	// for health checking this BackendService. Currently at most one health
	// check can be specified.
	// A health check must be specified unless the backend service uses an internet
	// or serverless NEG as a backend.
	// For internal load balancing, a URL to a HealthCheck resource must be specified instead.
	HealthChecks pulumi.StringPtrInput
	// Settings for enabling Cloud Identity Aware Proxy
	// Structure is documented below.
	Iap BackendServiceIapPtrInput
	// Indicates whether the backend service will be used with internal or
	// external load balancing. A backend service created for one type of
	// load balancing cannot be used with the other.
	// Default value is `EXTERNAL`.
	// Possible values are `EXTERNAL` and `INTERNAL_SELF_MANAGED`.
	LoadBalancingScheme pulumi.StringPtrInput
	// The load balancing algorithm used within the scope of the locality.
	// The possible values are -
	// * ROUND_ROBIN - This is a simple policy in which each healthy backend
	//   is selected in round robin order.
	// * LEAST_REQUEST - An O(1) algorithm which selects two random healthy
	//   hosts and picks the host which has fewer active requests.
	// * RING_HASH - The ring/modulo hash load balancer implements consistent
	//   hashing to backends. The algorithm has the property that the
	//   addition/removal of a host from a set of N hosts only affects
	//   1/N of the requests.
	// * RANDOM - The load balancer selects a random healthy host.
	// * ORIGINAL_DESTINATION - Backend host is selected based on the client
	//   connection metadata, i.e., connections are opened
	//   to the same address as the destination address of
	//   the incoming connection before the connection
	//   was redirected to the load balancer.
	// * MAGLEV - used as a drop in replacement for the ring hash load balancer.
	//   Maglev is not as stable as ring hash but has faster table lookup
	//   build times and host selection times. For more information about
	//   Maglev, refer to https://ai.google/research/pubs/pub44824
	//   This field is applicable only when the loadBalancingScheme is set to
	//   INTERNAL_SELF_MANAGED.
	//   Possible values are `ROUND_ROBIN`, `LEAST_REQUEST`, `RING_HASH`, `RANDOM`, `ORIGINAL_DESTINATION`, and `MAGLEV`.
	LocalityLbPolicy pulumi.StringPtrInput
	// This field denotes the logging options for the load balancer traffic served by this backend service.
	// If logging is enabled, logs will be exported to Stackdriver.
	// Structure is documented below.
	LogConfig BackendServiceLogConfigPtrInput
	// Name of the cookie.
	Name pulumi.StringPtrInput
	// Settings controlling eviction of unhealthy hosts from the load balancing pool.
	// This field is applicable only when the loadBalancingScheme is set
	// to INTERNAL_SELF_MANAGED.
	// Structure is documented below.
	OutlierDetection BackendServiceOutlierDetectionPtrInput
	// Name of backend port. The same name should appear in the instance
	// groups referenced by this service. Required when the load balancing
	// scheme is EXTERNAL.
	PortName pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// The protocol this BackendService uses to communicate with backends.
	// The default is HTTP. **NOTE**: HTTP2 is only valid for beta HTTP/2 load balancer
	// types and may result in errors if used with the GA API.
	// Possible values are `HTTP`, `HTTPS`, `HTTP2`, `TCP`, `SSL`, and `GRPC`.
	Protocol pulumi.StringPtrInput
	// The security policy associated with this backend service.
	SecurityPolicy pulumi.StringPtrInput
	// Type of session affinity to use. The default is NONE. Session affinity is
	// not applicable if the protocol is UDP.
	// Possible values are `NONE`, `CLIENT_IP`, `CLIENT_IP_PORT_PROTO`, `CLIENT_IP_PROTO`, `GENERATED_COOKIE`, `HEADER_FIELD`, and `HTTP_COOKIE`.
	SessionAffinity pulumi.StringPtrInput
	// How many seconds to wait for the backend before considering it a
	// failed request. Default is 30 seconds. Valid range is [1, 86400].
	TimeoutSec pulumi.IntPtrInput
}

func (BackendServiceArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*backendServiceArgs)(nil)).Elem()
}
