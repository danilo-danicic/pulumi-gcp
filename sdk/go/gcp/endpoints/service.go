// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package endpoints

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// This resource creates and rolls out a Cloud Endpoints service using OpenAPI or gRPC.  View the relevant docs for [OpenAPI](https://cloud.google.com/endpoints/docs/openapi/) and [gRPC](https://cloud.google.com/endpoints/docs/grpc/).
type Service struct {
	s *pulumi.ResourceState
}

// NewService registers a new resource with the given unique name, arguments, and options.
func NewService(ctx *pulumi.Context,
	name string, args *ServiceArgs, opts ...pulumi.ResourceOpt) (*Service, error) {
	if args == nil || args.ServiceName == nil {
		return nil, errors.New("missing required argument 'ServiceName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["grpcConfig"] = nil
		inputs["openapiConfig"] = nil
		inputs["project"] = nil
		inputs["protocOutput"] = nil
		inputs["protocOutputBase64"] = nil
		inputs["serviceName"] = nil
	} else {
		inputs["grpcConfig"] = args.GrpcConfig
		inputs["openapiConfig"] = args.OpenapiConfig
		inputs["project"] = args.Project
		inputs["protocOutput"] = args.ProtocOutput
		inputs["protocOutputBase64"] = args.ProtocOutputBase64
		inputs["serviceName"] = args.ServiceName
	}
	inputs["apis"] = nil
	inputs["configId"] = nil
	inputs["dnsAddress"] = nil
	inputs["endpoints"] = nil
	s, err := ctx.RegisterResource("gcp:endpoints/service:Service", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Service{s: s}, nil
}

// GetService gets an existing Service resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetService(ctx *pulumi.Context,
	name string, id pulumi.ID, state *ServiceState, opts ...pulumi.ResourceOpt) (*Service, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["apis"] = state.Apis
		inputs["configId"] = state.ConfigId
		inputs["dnsAddress"] = state.DnsAddress
		inputs["endpoints"] = state.Endpoints
		inputs["grpcConfig"] = state.GrpcConfig
		inputs["openapiConfig"] = state.OpenapiConfig
		inputs["project"] = state.Project
		inputs["protocOutput"] = state.ProtocOutput
		inputs["protocOutputBase64"] = state.ProtocOutputBase64
		inputs["serviceName"] = state.ServiceName
	}
	s, err := ctx.ReadResource("gcp:endpoints/service:Service", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &Service{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *Service) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *Service) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *Service) Apis() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["apis"])
}

func (r *Service) ConfigId() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["configId"])
}

func (r *Service) DnsAddress() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["dnsAddress"])
}

func (r *Service) Endpoints() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["endpoints"])
}

func (r *Service) GrpcConfig() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["grpcConfig"])
}

func (r *Service) OpenapiConfig() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["openapiConfig"])
}

func (r *Service) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

func (r *Service) ProtocOutput() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["protocOutput"])
}

func (r *Service) ProtocOutputBase64() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["protocOutputBase64"])
}

func (r *Service) ServiceName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["serviceName"])
}

// Input properties used for looking up and filtering Service resources.
type ServiceState struct {
	Apis interface{}
	ConfigId interface{}
	DnsAddress interface{}
	Endpoints interface{}
	GrpcConfig interface{}
	OpenapiConfig interface{}
	Project interface{}
	ProtocOutput interface{}
	ProtocOutputBase64 interface{}
	ServiceName interface{}
}

// The set of arguments for constructing a Service resource.
type ServiceArgs struct {
	GrpcConfig interface{}
	OpenapiConfig interface{}
	Project interface{}
	ProtocOutput interface{}
	ProtocOutputBase64 interface{}
	ServiceName interface{}
}
