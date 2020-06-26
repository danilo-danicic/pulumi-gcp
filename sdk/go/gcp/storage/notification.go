// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package storage

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

// Creates a new notification configuration on a specified bucket, establishing a flow of event notifications from GCS to a Cloud Pub/Sub topic.
//  For more information see
// [the official documentation](https://cloud.google.com/storage/docs/pubsub-notifications)
// and
// [API](https://cloud.google.com/storage/docs/json_api/v1/notifications).
//
// In order to enable notifications, a special Google Cloud Storage service account unique to the project
// must have the IAM permission "projects.topics.publish" for a Cloud Pub/Sub topic in the project. To get the service
// account's email address, use the `storage.getProjectServiceAccount` datasource's `emailAddress` value, and see below
// for an example of enabling notifications by granting the correct IAM permission. See
// [the notifications documentation](https://cloud.google.com/storage/docs/gsutil/commands/notification) for more details.
//
// > **NOTE**: This resource can affect your storage IAM policy. If you are using this in the same config as your storage IAM policy resources, consider
// making this resource dependent on those IAM resources via `dependsOn`. This will safeguard against errors due to IAM race conditions.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"fmt"
//
// 	"github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/pubsub"
// 	"github.com/pulumi/pulumi-gcp/sdk/v3/go/gcp/storage"
// 	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		gcsAccount, err := storage.GetProjectServiceAccount(ctx, nil, nil)
// 		if err != nil {
// 			return err
// 		}
// 		topic, err := pubsub.NewTopic(ctx, "topic", nil)
// 		if err != nil {
// 			return err
// 		}
// 		binding, err := pubsub.NewTopicIAMBinding(ctx, "binding", &pubsub.TopicIAMBindingArgs{
// 			Topic: topic.ID(),
// 			Role:  pulumi.String("roles/pubsub.publisher"),
// 			Members: pulumi.StringArray{
// 				pulumi.String(fmt.Sprintf("%v%v", "serviceAccount:", gcsAccount.EmailAddress)),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		bucket, err := storage.NewBucket(ctx, "bucket", nil)
// 		if err != nil {
// 			return err
// 		}
// 		_, err = storage.NewNotification(ctx, "notification", &storage.NotificationArgs{
// 			Bucket:        bucket.Name,
// 			PayloadFormat: pulumi.String("JSON_API_V1"),
// 			Topic:         topic.ID(),
// 			EventTypes: pulumi.StringArray{
// 				pulumi.String("OBJECT_FINALIZE"),
// 				pulumi.String("OBJECT_METADATA_UPDATE"),
// 			},
// 			CustomAttributes: pulumi.Map{
// 				"new-attribute": pulumi.String("new-attribute-value"),
// 			},
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
type Notification struct {
	pulumi.CustomResourceState

	// The name of the bucket.
	Bucket pulumi.StringOutput `pulumi:"bucket"`
	// A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
	CustomAttributes pulumi.StringMapOutput `pulumi:"customAttributes"`
	// List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
	EventTypes pulumi.StringArrayOutput `pulumi:"eventTypes"`
	// The ID of the created notification.
	NotificationId pulumi.StringOutput `pulumi:"notificationId"`
	// Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
	ObjectNamePrefix pulumi.StringPtrOutput `pulumi:"objectNamePrefix"`
	// The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
	PayloadFormat pulumi.StringOutput `pulumi:"payloadFormat"`
	// The URI of the created resource.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
	// The Cloud PubSub topic to which this subscription publishes. Expects either the
	// topic name, assumed to belong to the default GCP provider project, or the project-level name,
	// i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
	// you will need to use the project-level name.
	Topic pulumi.StringOutput `pulumi:"topic"`
}

// NewNotification registers a new resource with the given unique name, arguments, and options.
func NewNotification(ctx *pulumi.Context,
	name string, args *NotificationArgs, opts ...pulumi.ResourceOption) (*Notification, error) {
	if args == nil || args.Bucket == nil {
		return nil, errors.New("missing required argument 'Bucket'")
	}
	if args == nil || args.PayloadFormat == nil {
		return nil, errors.New("missing required argument 'PayloadFormat'")
	}
	if args == nil || args.Topic == nil {
		return nil, errors.New("missing required argument 'Topic'")
	}
	if args == nil {
		args = &NotificationArgs{}
	}
	var resource Notification
	err := ctx.RegisterResource("gcp:storage/notification:Notification", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetNotification gets an existing Notification resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetNotification(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *NotificationState, opts ...pulumi.ResourceOption) (*Notification, error) {
	var resource Notification
	err := ctx.ReadResource("gcp:storage/notification:Notification", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Notification resources.
type notificationState struct {
	// The name of the bucket.
	Bucket *string `pulumi:"bucket"`
	// A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
	CustomAttributes map[string]string `pulumi:"customAttributes"`
	// List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
	EventTypes []string `pulumi:"eventTypes"`
	// The ID of the created notification.
	NotificationId *string `pulumi:"notificationId"`
	// Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
	ObjectNamePrefix *string `pulumi:"objectNamePrefix"`
	// The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
	PayloadFormat *string `pulumi:"payloadFormat"`
	// The URI of the created resource.
	SelfLink *string `pulumi:"selfLink"`
	// The Cloud PubSub topic to which this subscription publishes. Expects either the
	// topic name, assumed to belong to the default GCP provider project, or the project-level name,
	// i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
	// you will need to use the project-level name.
	Topic *string `pulumi:"topic"`
}

type NotificationState struct {
	// The name of the bucket.
	Bucket pulumi.StringPtrInput
	// A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
	CustomAttributes pulumi.StringMapInput
	// List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
	EventTypes pulumi.StringArrayInput
	// The ID of the created notification.
	NotificationId pulumi.StringPtrInput
	// Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
	ObjectNamePrefix pulumi.StringPtrInput
	// The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
	PayloadFormat pulumi.StringPtrInput
	// The URI of the created resource.
	SelfLink pulumi.StringPtrInput
	// The Cloud PubSub topic to which this subscription publishes. Expects either the
	// topic name, assumed to belong to the default GCP provider project, or the project-level name,
	// i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
	// you will need to use the project-level name.
	Topic pulumi.StringPtrInput
}

func (NotificationState) ElementType() reflect.Type {
	return reflect.TypeOf((*notificationState)(nil)).Elem()
}

type notificationArgs struct {
	// The name of the bucket.
	Bucket string `pulumi:"bucket"`
	// A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
	CustomAttributes map[string]string `pulumi:"customAttributes"`
	// List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
	EventTypes []string `pulumi:"eventTypes"`
	// Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
	ObjectNamePrefix *string `pulumi:"objectNamePrefix"`
	// The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
	PayloadFormat string `pulumi:"payloadFormat"`
	// The Cloud PubSub topic to which this subscription publishes. Expects either the
	// topic name, assumed to belong to the default GCP provider project, or the project-level name,
	// i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
	// you will need to use the project-level name.
	Topic string `pulumi:"topic"`
}

// The set of arguments for constructing a Notification resource.
type NotificationArgs struct {
	// The name of the bucket.
	Bucket pulumi.StringInput
	// A set of key/value attribute pairs to attach to each Cloud PubSub message published for this notification subscription
	CustomAttributes pulumi.StringMapInput
	// List of event type filters for this notification config. If not specified, Cloud Storage will send notifications for all event types. The valid types are: `"OBJECT_FINALIZE"`, `"OBJECT_METADATA_UPDATE"`, `"OBJECT_DELETE"`, `"OBJECT_ARCHIVE"`
	EventTypes pulumi.StringArrayInput
	// Specifies a prefix path filter for this notification config. Cloud Storage will only send notifications for objects in this bucket whose names begin with the specified prefix.
	ObjectNamePrefix pulumi.StringPtrInput
	// The desired content of the Payload. One of `"JSON_API_V1"` or `"NONE"`.
	PayloadFormat pulumi.StringInput
	// The Cloud PubSub topic to which this subscription publishes. Expects either the
	// topic name, assumed to belong to the default GCP provider project, or the project-level name,
	// i.e. `projects/my-gcp-project/topics/my-topic` or `my-topic`. If the project is not set in the provider,
	// you will need to use the project-level name.
	Topic pulumi.StringInput
}

func (NotificationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*notificationArgs)(nil)).Elem()
}
