# Terraform::Google::PubsubSubscriptionIamMember

CloudFormation equivalent of google_pubsub_subscription_iam_member

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Google::PubsubSubscriptionIamMember",
    "Properties" : {
        "<a href="#member" title="Member">Member</a>" : <i>String</i>,
        "<a href="#project" title="Project">Project</a>" : <i>String</i>,
        "<a href="#role" title="Role">Role</a>" : <i>String</i>,
        "<a href="#subscription" title="Subscription">Subscription</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Google::PubsubSubscriptionIamMember
Properties:
    <a href="#member" title="Member">Member</a>: <i>String</i>
    <a href="#project" title="Project">Project</a>: <i>String</i>
    <a href="#role" title="Role">Role</a>: <i>String</i>
    <a href="#subscription" title="Subscription">Subscription</a>: <i>String</i>
</pre>

## Properties

#### Member

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Project

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Role

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Subscription

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Etag

Returns the <code>Etag</code> value.

#### Id

Returns the <code>Id</code> value.
