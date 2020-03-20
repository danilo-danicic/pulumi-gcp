// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package dataproc

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Manages a job resource within a Dataproc cluster within GCE. For more information see
// [the official dataproc documentation](https://cloud.google.com/dataproc/).
//
// !> **Note:** This resource does not support 'update' and changing any attributes will cause the resource to be recreated.
//
// > This content is derived from https://github.com/terraform-providers/terraform-provider-google/blob/master/website/docs/r/dataproc_job.html.markdown.
type Job struct {
	pulumi.CustomResourceState

	// If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
	DriverControlsFilesUri pulumi.StringOutput `pulumi:"driverControlsFilesUri"`
	// A URI pointing to the location of the stdout of the job's driver program.
	DriverOutputResourceUri pulumi.StringOutput `pulumi:"driverOutputResourceUri"`
	// By default, you can only delete inactive jobs within
	// Dataproc. Setting this to true, and calling destroy, will ensure that the
	// job is first cancelled before issuing the delete.
	ForceDelete  pulumi.BoolPtrOutput     `pulumi:"forceDelete"`
	HadoopConfig JobHadoopConfigPtrOutput `pulumi:"hadoopConfig"`
	HiveConfig   JobHiveConfigPtrOutput   `pulumi:"hiveConfig"`
	// The list of labels (key/value pairs) to add to the job.
	Labels    pulumi.StringMapOutput `pulumi:"labels"`
	PigConfig JobPigConfigPtrOutput  `pulumi:"pigConfig"`
	Placement JobPlacementOutput     `pulumi:"placement"`
	// The project in which the `cluster` can be found and jobs
	// subsequently run against. If it is not provided, the provider project is used.
	Project       pulumi.StringOutput       `pulumi:"project"`
	PysparkConfig JobPysparkConfigPtrOutput `pulumi:"pysparkConfig"`
	Reference     JobReferenceOutput        `pulumi:"reference"`
	// The Cloud Dataproc region. This essentially determines which clusters are available
	// for this job to be submitted to. If not specified, defaults to `global`.
	Region pulumi.StringPtrOutput `pulumi:"region"`
	// Optional. Job scheduling configuration.
	Scheduling     JobSchedulingPtrOutput     `pulumi:"scheduling"`
	SparkConfig    JobSparkConfigPtrOutput    `pulumi:"sparkConfig"`
	SparksqlConfig JobSparksqlConfigPtrOutput `pulumi:"sparksqlConfig"`
	Status         JobStatusOutput            `pulumi:"status"`
}

// NewJob registers a new resource with the given unique name, arguments, and options.
func NewJob(ctx *pulumi.Context,
	name string, args *JobArgs, opts ...pulumi.ResourceOption) (*Job, error) {
	if args == nil || args.Placement == nil {
		return nil, errors.New("missing required argument 'Placement'")
	}
	if args == nil {
		args = &JobArgs{}
	}
	var resource Job
	err := ctx.RegisterResource("gcp:dataproc/job:Job", name, args, &resource, opts...)
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
	err := ctx.ReadResource("gcp:dataproc/job:Job", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Job resources.
type jobState struct {
	// If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
	DriverControlsFilesUri *string `pulumi:"driverControlsFilesUri"`
	// A URI pointing to the location of the stdout of the job's driver program.
	DriverOutputResourceUri *string `pulumi:"driverOutputResourceUri"`
	// By default, you can only delete inactive jobs within
	// Dataproc. Setting this to true, and calling destroy, will ensure that the
	// job is first cancelled before issuing the delete.
	ForceDelete  *bool            `pulumi:"forceDelete"`
	HadoopConfig *JobHadoopConfig `pulumi:"hadoopConfig"`
	HiveConfig   *JobHiveConfig   `pulumi:"hiveConfig"`
	// The list of labels (key/value pairs) to add to the job.
	Labels    map[string]string `pulumi:"labels"`
	PigConfig *JobPigConfig     `pulumi:"pigConfig"`
	Placement *JobPlacement     `pulumi:"placement"`
	// The project in which the `cluster` can be found and jobs
	// subsequently run against. If it is not provided, the provider project is used.
	Project       *string           `pulumi:"project"`
	PysparkConfig *JobPysparkConfig `pulumi:"pysparkConfig"`
	Reference     *JobReference     `pulumi:"reference"`
	// The Cloud Dataproc region. This essentially determines which clusters are available
	// for this job to be submitted to. If not specified, defaults to `global`.
	Region *string `pulumi:"region"`
	// Optional. Job scheduling configuration.
	Scheduling     *JobScheduling     `pulumi:"scheduling"`
	SparkConfig    *JobSparkConfig    `pulumi:"sparkConfig"`
	SparksqlConfig *JobSparksqlConfig `pulumi:"sparksqlConfig"`
	Status         *JobStatus         `pulumi:"status"`
}

type JobState struct {
	// If present, the location of miscellaneous control files which may be used as part of job setup and handling. If not present, control files may be placed in the same location as driver_output_uri.
	DriverControlsFilesUri pulumi.StringPtrInput
	// A URI pointing to the location of the stdout of the job's driver program.
	DriverOutputResourceUri pulumi.StringPtrInput
	// By default, you can only delete inactive jobs within
	// Dataproc. Setting this to true, and calling destroy, will ensure that the
	// job is first cancelled before issuing the delete.
	ForceDelete  pulumi.BoolPtrInput
	HadoopConfig JobHadoopConfigPtrInput
	HiveConfig   JobHiveConfigPtrInput
	// The list of labels (key/value pairs) to add to the job.
	Labels    pulumi.StringMapInput
	PigConfig JobPigConfigPtrInput
	Placement JobPlacementPtrInput
	// The project in which the `cluster` can be found and jobs
	// subsequently run against. If it is not provided, the provider project is used.
	Project       pulumi.StringPtrInput
	PysparkConfig JobPysparkConfigPtrInput
	Reference     JobReferencePtrInput
	// The Cloud Dataproc region. This essentially determines which clusters are available
	// for this job to be submitted to. If not specified, defaults to `global`.
	Region pulumi.StringPtrInput
	// Optional. Job scheduling configuration.
	Scheduling     JobSchedulingPtrInput
	SparkConfig    JobSparkConfigPtrInput
	SparksqlConfig JobSparksqlConfigPtrInput
	Status         JobStatusPtrInput
}

func (JobState) ElementType() reflect.Type {
	return reflect.TypeOf((*jobState)(nil)).Elem()
}

type jobArgs struct {
	// By default, you can only delete inactive jobs within
	// Dataproc. Setting this to true, and calling destroy, will ensure that the
	// job is first cancelled before issuing the delete.
	ForceDelete  *bool            `pulumi:"forceDelete"`
	HadoopConfig *JobHadoopConfig `pulumi:"hadoopConfig"`
	HiveConfig   *JobHiveConfig   `pulumi:"hiveConfig"`
	// The list of labels (key/value pairs) to add to the job.
	Labels    map[string]string `pulumi:"labels"`
	PigConfig *JobPigConfig     `pulumi:"pigConfig"`
	Placement JobPlacement      `pulumi:"placement"`
	// The project in which the `cluster` can be found and jobs
	// subsequently run against. If it is not provided, the provider project is used.
	Project       *string           `pulumi:"project"`
	PysparkConfig *JobPysparkConfig `pulumi:"pysparkConfig"`
	Reference     *JobReference     `pulumi:"reference"`
	// The Cloud Dataproc region. This essentially determines which clusters are available
	// for this job to be submitted to. If not specified, defaults to `global`.
	Region *string `pulumi:"region"`
	// Optional. Job scheduling configuration.
	Scheduling     *JobScheduling     `pulumi:"scheduling"`
	SparkConfig    *JobSparkConfig    `pulumi:"sparkConfig"`
	SparksqlConfig *JobSparksqlConfig `pulumi:"sparksqlConfig"`
}

// The set of arguments for constructing a Job resource.
type JobArgs struct {
	// By default, you can only delete inactive jobs within
	// Dataproc. Setting this to true, and calling destroy, will ensure that the
	// job is first cancelled before issuing the delete.
	ForceDelete  pulumi.BoolPtrInput
	HadoopConfig JobHadoopConfigPtrInput
	HiveConfig   JobHiveConfigPtrInput
	// The list of labels (key/value pairs) to add to the job.
	Labels    pulumi.StringMapInput
	PigConfig JobPigConfigPtrInput
	Placement JobPlacementInput
	// The project in which the `cluster` can be found and jobs
	// subsequently run against. If it is not provided, the provider project is used.
	Project       pulumi.StringPtrInput
	PysparkConfig JobPysparkConfigPtrInput
	Reference     JobReferencePtrInput
	// The Cloud Dataproc region. This essentially determines which clusters are available
	// for this job to be submitted to. If not specified, defaults to `global`.
	Region pulumi.StringPtrInput
	// Optional. Job scheduling configuration.
	Scheduling     JobSchedulingPtrInput
	SparkConfig    JobSparkConfigPtrInput
	SparksqlConfig JobSparksqlConfigPtrInput
}

func (JobArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*jobArgs)(nil)).Elem()
}
