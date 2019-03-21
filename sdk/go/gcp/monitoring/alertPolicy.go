// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package monitoring

import (
	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// A description of the conditions under which some aspect of your system is
// considered to be "unhealthy" and the ways to notify people or services
// about this state.
// 
// 
// To get more information about AlertPolicy, see:
// 
// * [API documentation](https://cloud.google.com/monitoring/api/ref_v3/rest/v3/projects.alertPolicies)
// * How-to Guides
//     * [Official Documentation](https://cloud.google.com/monitoring/alerts/)
// 
// <div class = "oics-button" style="float: right; margin: 0 0 -15px">
//   <a href="https://console.cloud.google.com/cloudshell/open?cloudshell_git_repo=https%3A%2F%2Fgithub.com%2Fterraform-google-modules%2Fdocs-examples.git&cloudshell_working_dir=monitoring_alert_policy_basic&cloudshell_image=gcr.io%2Fgraphite-cloud-shell-images%2Fterraform%3Alatest&open_in_editor=main.tf&cloudshell_print=.%2Fmotd&cloudshell_tutorial=.%2Ftutorial.md" target="_blank">
//     <img alt="Open in Cloud Shell" src="//gstatic.com/cloudssh/images/open-btn.svg" style="max-height: 44px; margin: 32px auto; max-width: 100%;">
//   </a>
// </div>
type AlertPolicy struct {
	s *pulumi.ResourceState
}

// NewAlertPolicy registers a new resource with the given unique name, arguments, and options.
func NewAlertPolicy(ctx *pulumi.Context,
	name string, args *AlertPolicyArgs, opts ...pulumi.ResourceOpt) (*AlertPolicy, error) {
	if args == nil || args.Combiner == nil {
		return nil, errors.New("missing required argument 'Combiner'")
	}
	if args == nil || args.Conditions == nil {
		return nil, errors.New("missing required argument 'Conditions'")
	}
	if args == nil || args.DisplayName == nil {
		return nil, errors.New("missing required argument 'DisplayName'")
	}
	inputs := make(map[string]interface{})
	if args == nil {
		inputs["combiner"] = nil
		inputs["conditions"] = nil
		inputs["displayName"] = nil
		inputs["documentation"] = nil
		inputs["enabled"] = nil
		inputs["labels"] = nil
		inputs["notificationChannels"] = nil
		inputs["project"] = nil
	} else {
		inputs["combiner"] = args.Combiner
		inputs["conditions"] = args.Conditions
		inputs["displayName"] = args.DisplayName
		inputs["documentation"] = args.Documentation
		inputs["enabled"] = args.Enabled
		inputs["labels"] = args.Labels
		inputs["notificationChannels"] = args.NotificationChannels
		inputs["project"] = args.Project
	}
	inputs["creationRecord"] = nil
	inputs["name"] = nil
	s, err := ctx.RegisterResource("gcp:monitoring/alertPolicy:AlertPolicy", name, true, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AlertPolicy{s: s}, nil
}

// GetAlertPolicy gets an existing AlertPolicy resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAlertPolicy(ctx *pulumi.Context,
	name string, id pulumi.ID, state *AlertPolicyState, opts ...pulumi.ResourceOpt) (*AlertPolicy, error) {
	inputs := make(map[string]interface{})
	if state != nil {
		inputs["combiner"] = state.Combiner
		inputs["conditions"] = state.Conditions
		inputs["creationRecord"] = state.CreationRecord
		inputs["displayName"] = state.DisplayName
		inputs["documentation"] = state.Documentation
		inputs["enabled"] = state.Enabled
		inputs["labels"] = state.Labels
		inputs["name"] = state.Name
		inputs["notificationChannels"] = state.NotificationChannels
		inputs["project"] = state.Project
	}
	s, err := ctx.ReadResource("gcp:monitoring/alertPolicy:AlertPolicy", name, id, inputs, opts...)
	if err != nil {
		return nil, err
	}
	return &AlertPolicy{s: s}, nil
}

// URN is this resource's unique name assigned by Pulumi.
func (r *AlertPolicy) URN() *pulumi.URNOutput {
	return r.s.URN()
}

// ID is this resource's unique identifier assigned by its provider.
func (r *AlertPolicy) ID() *pulumi.IDOutput {
	return r.s.ID()
}

func (r *AlertPolicy) Combiner() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["combiner"])
}

func (r *AlertPolicy) Conditions() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["conditions"])
}

func (r *AlertPolicy) CreationRecord() *pulumi.Output {
	return r.s.State["creationRecord"]
}

func (r *AlertPolicy) DisplayName() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["displayName"])
}

func (r *AlertPolicy) Documentation() *pulumi.Output {
	return r.s.State["documentation"]
}

func (r *AlertPolicy) Enabled() *pulumi.BoolOutput {
	return (*pulumi.BoolOutput)(r.s.State["enabled"])
}

func (r *AlertPolicy) Labels() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["labels"])
}

func (r *AlertPolicy) Name() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["name"])
}

func (r *AlertPolicy) NotificationChannels() *pulumi.ArrayOutput {
	return (*pulumi.ArrayOutput)(r.s.State["notificationChannels"])
}

func (r *AlertPolicy) Project() *pulumi.StringOutput {
	return (*pulumi.StringOutput)(r.s.State["project"])
}

// Input properties used for looking up and filtering AlertPolicy resources.
type AlertPolicyState struct {
	Combiner interface{}
	Conditions interface{}
	CreationRecord interface{}
	DisplayName interface{}
	Documentation interface{}
	Enabled interface{}
	Labels interface{}
	Name interface{}
	NotificationChannels interface{}
	Project interface{}
}

// The set of arguments for constructing a AlertPolicy resource.
type AlertPolicyArgs struct {
	Combiner interface{}
	Conditions interface{}
	DisplayName interface{}
	Documentation interface{}
	Enabled interface{}
	Labels interface{}
	NotificationChannels interface{}
	Project interface{}
}
