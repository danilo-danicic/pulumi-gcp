// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package pubsub

import (
	"fmt"

	"github.com/blang/semver"
	"github.com/pulumi/pulumi-gcp/sdk/v4/go/gcp"
	"github.com/pulumi/pulumi/sdk/v2/go/pulumi"
)

type module struct {
	version semver.Version
}

func (m *module) Version() semver.Version {
	return m.version
}

func (m *module) Construct(ctx *pulumi.Context, name, typ, urn string) (r pulumi.Resource, err error) {
	switch typ {
	case "gcp:pubsub/liteSubscription:LiteSubscription":
		r, err = NewLiteSubscription(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/liteTopic:LiteTopic":
		r, err = NewLiteTopic(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/subscription:Subscription":
		r, err = NewSubscription(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/subscriptionIAMBinding:SubscriptionIAMBinding":
		r, err = NewSubscriptionIAMBinding(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/subscriptionIAMMember:SubscriptionIAMMember":
		r, err = NewSubscriptionIAMMember(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/subscriptionIAMPolicy:SubscriptionIAMPolicy":
		r, err = NewSubscriptionIAMPolicy(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/topic:Topic":
		r, err = NewTopic(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/topicIAMBinding:TopicIAMBinding":
		r, err = NewTopicIAMBinding(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/topicIAMMember:TopicIAMMember":
		r, err = NewTopicIAMMember(ctx, name, nil, pulumi.URN_(urn))
	case "gcp:pubsub/topicIAMPolicy:TopicIAMPolicy":
		r, err = NewTopicIAMPolicy(ctx, name, nil, pulumi.URN_(urn))
	default:
		return nil, fmt.Errorf("unknown resource type: %s", typ)
	}

	return
}

func init() {
	version, err := gcp.PkgVersion()
	if err != nil {
		fmt.Println("failed to determine package version. defaulting to v1: %v", err)
	}
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/liteSubscription",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/liteTopic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/subscription",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/subscriptionIAMBinding",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/subscriptionIAMMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/subscriptionIAMPolicy",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/topic",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/topicIAMBinding",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/topicIAMMember",
		&module{version},
	)
	pulumi.RegisterResourceModule(
		"gcp",
		"pubsub/topicIAMPolicy",
		&module{version},
	)
}
