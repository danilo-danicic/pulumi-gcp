// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package kms

import (
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// Provides access to a Google Cloud Platform KMS CryptoKey. For more information see
// [the official documentation](https://cloud.google.com/kms/docs/object-hierarchy#key)
// and
// [API](https://cloud.google.com/kms/docs/reference/rest/v1/projects.locations.keyRings.cryptoKeys).
// 
// A CryptoKey is an interface to key material which can be used to encrypt and decrypt data. A CryptoKey belongs to a
// Google Cloud KMS KeyRing.
func LookupKMSCryptoKey(ctx *pulumi.Context, args *GetKMSCryptoKeyArgs) (*GetKMSCryptoKeyResult, error) {
	inputs := make(map[string]interface{})
	if args != nil {
		inputs["keyRing"] = args.KeyRing
		inputs["name"] = args.Name
	}
	outputs, err := ctx.Invoke("gcp:kms/getKMSCryptoKey:getKMSCryptoKey", inputs)
	if err != nil {
		return nil, err
	}
	return &GetKMSCryptoKeyResult{
		KeyRing: outputs["keyRing"],
		Name: outputs["name"],
		RotationPeriod: outputs["rotationPeriod"],
		SelfLink: outputs["selfLink"],
		VersionTemplates: outputs["versionTemplates"],
		Id: outputs["id"],
	}, nil
}

// A collection of arguments for invoking getKMSCryptoKey.
type GetKMSCryptoKeyArgs struct {
	// The `self_link` of the Google Cloud Platform KeyRing to which the key belongs.
	KeyRing interface{}
	// The CryptoKey's name.
	// A CryptoKey’s name belonging to the specified Google Cloud Platform KeyRing and match the regular expression `[a-zA-Z0-9_-]{1,63}`
	Name interface{}
}

// A collection of values returned by getKMSCryptoKey.
type GetKMSCryptoKeyResult struct {
	KeyRing interface{}
	Name interface{}
	// Every time this period passes, generate a new CryptoKeyVersion and set it as
	// the primary. The first rotation will take place after the specified period. The rotation period has the format
	// of a decimal number with up to 9 fractional digits, followed by the letter s (seconds).
	RotationPeriod interface{}
	// The self link of the created CryptoKey. Its format is `projects/{projectId}/locations/{location}/keyRings/{keyRingName}/cryptoKeys/{cryptoKeyName}`.
	SelfLink interface{}
	VersionTemplates interface{}
	// id is the provider-assigned unique ID for this managed resource.
	Id interface{}
}
