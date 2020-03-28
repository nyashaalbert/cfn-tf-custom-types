# Terraform::Icinga2::Service

Configures an Icinga2 service resource. This allows service to be configured, updated,
and deleted.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::Icinga2::Service",
    "Properties" : {
        "<a href="#checkcommand" title="CheckCommand">CheckCommand</a>" : <i>String</i>,
        "<a href="#hostname" title="Hostname">Hostname</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#vars" title="Vars">Vars</a>" : <i>[ <a href="vars.md">Vars</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::Icinga2::Service
Properties:
    <a href="#checkcommand" title="CheckCommand">CheckCommand</a>: <i>String</i>
    <a href="#hostname" title="Hostname">Hostname</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#vars" title="Vars">Vars</a>: <i>
      - <a href="vars.md">Vars</a></i>
</pre>

## Properties

#### CheckCommand

The name of an existing Icinga2 CheckCommand object that is used to determine if the service is available on the host.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Hostname

The host to check the service's status on.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the Service object.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Vars

A mapping of variables to assign to the service.

_Required_: No

_Type_: List of <a href="vars.md">Vars</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Id

Returns the <code>Id</code> value.
