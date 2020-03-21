# Terraform::Vault::OktaAuthBackendUser

CloudFormation equivalent of vault_okta_auth_backend_user

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Vault::OktaAuthBackendUser",
    "Properties" : {
        "<a href="#groups" title="Groups">Groups</a>" : <i>[ String, ... ]</i>,
        "<a href="#id" title="Id">Id</a>" : <i>String</i>,
        "<a href="#path" title="Path">Path</a>" : <i>String</i>,
        "<a href="#policies" title="Policies">Policies</a>" : <i>[ String, ... ]</i>,
        "<a href="#username" title="Username">Username</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Vault::OktaAuthBackendUser
Properties:
    <a href="#groups" title="Groups">Groups</a>: <i>
      - String</i>
    <a href="#id" title="Id">Id</a>: <i>String</i>
    <a href="#path" title="Path">Path</a>: <i>String</i>
    <a href="#policies" title="Policies">Policies</a>: <i>
      - String</i>
    <a href="#username" title="Username">Username</a>: <i>String</i>
</pre>

## Properties

#### Groups

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Id

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Path

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Policies

_Required_: No

_Type_: List of String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Username

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
