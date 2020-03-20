// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package cloudscheduler

import (
	"reflect"

	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

type Job struct {
	pulumi.CustomResourceState

	// App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
	// instance
	AppEngineHttpTarget JobAppEngineHttpTargetPtrOutput `pulumi:"appEngineHttpTarget"`
	// The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
	// and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
	// Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
	// targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
	// in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
	AttemptDeadline pulumi.StringPtrOutput `pulumi:"attemptDeadline"`
	// A human-readable description for the job. This string must not contain more than 500 characters.
	Description pulumi.StringPtrOutput `pulumi:"description"`
	// HTTP target. If the job providers a http_target the cron will send a request to the targeted url
	HttpTarget JobHttpTargetPtrOutput `pulumi:"httpTarget"`
	// The name of the job.
	Name pulumi.StringOutput `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringOutput `pulumi:"project"`
	// Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
	PubsubTarget JobPubsubTargetPtrOutput `pulumi:"pubsubTarget"`
	// Region where the scheduler job resides
	Region pulumi.StringOutput `pulumi:"region"`
	// By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
	// then it will be retried with exponential backoff according to the settings
	RetryConfig JobRetryConfigPtrOutput `pulumi:"retryConfig"`
	// Describes the schedule on which the job will be executed.
	Schedule pulumi.StringPtrOutput `pulumi:"schedule"`
	// Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
	// tz database.
	TimeZone pulumi.StringPtrOutput `pulumi:"timeZone"`
}

// NewJob registers a new resource with the given unique name, arguments, and options.
func NewJob(ctx *pulumi.Context,
	name string, args *JobArgs, opts ...pulumi.ResourceOption) (*Job, error) {
	if args == nil {
		args = &JobArgs{}
	}
	var resource Job
	err := ctx.RegisterResource("gcp:cloudscheduler/job:Job", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetJob gets an existing Job resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetJob(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *JobState, opts ...pulumi.ResourceOption) (*Job, error) {
	var resource Job
	err := ctx.ReadResource("gcp:cloudscheduler/job:Job", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Job resources.
type jobState struct {
	// App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
	// instance
	AppEngineHttpTarget *JobAppEngineHttpTarget `pulumi:"appEngineHttpTarget"`
	// The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
	// and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
	// Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
	// targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
	// in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
	AttemptDeadline *string `pulumi:"attemptDeadline"`
	// A human-readable description for the job. This string must not contain more than 500 characters.
	Description *string `pulumi:"description"`
	// HTTP target. If the job providers a http_target the cron will send a request to the targeted url
	HttpTarget *JobHttpTarget `pulumi:"httpTarget"`
	// The name of the job.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
	PubsubTarget *JobPubsubTarget `pulumi:"pubsubTarget"`
	// Region where the scheduler job resides
	Region *string `pulumi:"region"`
	// By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
	// then it will be retried with exponential backoff according to the settings
	RetryConfig *JobRetryConfig `pulumi:"retryConfig"`
	// Describes the schedule on which the job will be executed.
	Schedule *string `pulumi:"schedule"`
	// Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
	// tz database.
	TimeZone *string `pulumi:"timeZone"`
}

type JobState struct {
	// App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
	// instance
	AppEngineHttpTarget JobAppEngineHttpTargetPtrInput
	// The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
	// and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
	// Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
	// targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
	// in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
	AttemptDeadline pulumi.StringPtrInput
	// A human-readable description for the job. This string must not contain more than 500 characters.
	Description pulumi.StringPtrInput
	// HTTP target. If the job providers a http_target the cron will send a request to the targeted url
	HttpTarget JobHttpTargetPtrInput
	// The name of the job.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
	PubsubTarget JobPubsubTargetPtrInput
	// Region where the scheduler job resides
	Region pulumi.StringPtrInput
	// By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
	// then it will be retried with exponential backoff according to the settings
	RetryConfig JobRetryConfigPtrInput
	// Describes the schedule on which the job will be executed.
	Schedule pulumi.StringPtrInput
	// Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
	// tz database.
	TimeZone pulumi.StringPtrInput
}

func (JobState) ElementType() reflect.Type {
	return reflect.TypeOf((*jobState)(nil)).Elem()
}

type jobArgs struct {
	// App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
	// instance
	AppEngineHttpTarget *JobAppEngineHttpTarget `pulumi:"appEngineHttpTarget"`
	// The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
	// and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
	// Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
	// targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
	// in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
	AttemptDeadline *string `pulumi:"attemptDeadline"`
	// A human-readable description for the job. This string must not contain more than 500 characters.
	Description *string `pulumi:"description"`
	// HTTP target. If the job providers a http_target the cron will send a request to the targeted url
	HttpTarget *JobHttpTarget `pulumi:"httpTarget"`
	// The name of the job.
	Name *string `pulumi:"name"`
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project *string `pulumi:"project"`
	// Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
	PubsubTarget *JobPubsubTarget `pulumi:"pubsubTarget"`
	// Region where the scheduler job resides
	Region *string `pulumi:"region"`
	// By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
	// then it will be retried with exponential backoff according to the settings
	RetryConfig *JobRetryConfig `pulumi:"retryConfig"`
	// Describes the schedule on which the job will be executed.
	Schedule *string `pulumi:"schedule"`
	// Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
	// tz database.
	TimeZone *string `pulumi:"timeZone"`
}

// The set of arguments for constructing a Job resource.
type JobArgs struct {
	// App Engine HTTP target. If the job providers a App Engine HTTP target the cron will send a request to the service
	// instance
	AppEngineHttpTarget JobAppEngineHttpTargetPtrInput
	// The deadline for job attempts. If the request handler does not respond by this deadline then the request is cancelled
	// and the attempt is marked as a DEADLINE_EXCEEDED failure. The failed attempt can be viewed in execution logs. Cloud
	// Scheduler will retry the job according to the RetryConfig. The allowed duration for this deadline is: * For HTTP
	// targets, between 15 seconds and 30 minutes. * For App Engine HTTP targets, between 15 seconds and 24 hours. A duration
	// in seconds with up to nine fractional digits, terminated by 's'. Example: "3.5s"
	AttemptDeadline pulumi.StringPtrInput
	// A human-readable description for the job. This string must not contain more than 500 characters.
	Description pulumi.StringPtrInput
	// HTTP target. If the job providers a http_target the cron will send a request to the targeted url
	HttpTarget JobHttpTargetPtrInput
	// The name of the job.
	Name pulumi.StringPtrInput
	// The ID of the project in which the resource belongs.
	// If it is not provided, the provider project is used.
	Project pulumi.StringPtrInput
	// Pub/Sub target If the job providers a Pub/Sub target the cron will publish a message to the provided topic
	PubsubTarget JobPubsubTargetPtrInput
	// Region where the scheduler job resides
	Region pulumi.StringPtrInput
	// By default, if a job does not complete successfully, meaning that an acknowledgement is not received from the handler,
	// then it will be retried with exponential backoff according to the settings
	RetryConfig JobRetryConfigPtrInput
	// Describes the schedule on which the job will be executed.
	Schedule pulumi.StringPtrInput
	// Specifies the time zone to be used in interpreting schedule. The value of this field must be a time zone name from the
	// tz database.
	TimeZone pulumi.StringPtrInput
}

func (JobArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*jobArgs)(nil)).Elem()
}
