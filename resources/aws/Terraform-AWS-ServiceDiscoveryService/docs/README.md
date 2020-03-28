# Terraform::AWS::ServiceDiscoveryService

Provides a Service Discovery Service resource.

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::ServiceDiscoveryService",
    "Properties" : {
        "<a href="#description" title="Description">Description</a>" : <i>String</i>,
        "<a href="#name" title="Name">Name</a>" : <i>String</i>,
        "<a href="#namespaceid" title="NamespaceId">NamespaceId</a>" : <i>String</i>,
        "<a href="#dnsconfig" title="DnsConfig">DnsConfig</a>" : <i>[ <a href="dnsconfig.md">DnsConfig</a>, ... ]</i>,
        "<a href="#healthcheckconfig" title="HealthCheckConfig">HealthCheckConfig</a>" : <i>[ <a href="healthcheckconfig.md">HealthCheckConfig</a>, ... ]</i>,
        "<a href="#healthcheckcustomconfig" title="HealthCheckCustomConfig">HealthCheckCustomConfig</a>" : <i>[ <a href="healthcheckcustomconfig.md">HealthCheckCustomConfig</a>, ... ]</i>,
        "<a href="#dnsrecords" title="DnsRecords">DnsRecords</a>" : <i>[ <a href="dnsrecords.md">DnsRecords</a>, ... ]</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::ServiceDiscoveryService
Properties:
    <a href="#description" title="Description">Description</a>: <i>String</i>
    <a href="#name" title="Name">Name</a>: <i>String</i>
    <a href="#namespaceid" title="NamespaceId">NamespaceId</a>: <i>String</i>
    <a href="#dnsconfig" title="DnsConfig">DnsConfig</a>: <i>
      - <a href="dnsconfig.md">DnsConfig</a></i>
    <a href="#healthcheckconfig" title="HealthCheckConfig">HealthCheckConfig</a>: <i>
      - <a href="healthcheckconfig.md">HealthCheckConfig</a></i>
    <a href="#healthcheckcustomconfig" title="HealthCheckCustomConfig">HealthCheckCustomConfig</a>: <i>
      - <a href="healthcheckcustomconfig.md">HealthCheckCustomConfig</a></i>
    <a href="#dnsrecords" title="DnsRecords">DnsRecords</a>: <i>
      - <a href="dnsrecords.md">DnsRecords</a></i>
</pre>

## Properties

#### Description

The description of the service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### Name

The name of the service.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### NamespaceId

The ID of the namespace that you want to use to create the service.

_Required_: No

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsConfig

_Required_: No

_Type_: List of <a href="dnsconfig.md">DnsConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckConfig

_Required_: No

_Type_: List of <a href="healthcheckconfig.md">HealthCheckConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### HealthCheckCustomConfig

_Required_: No

_Type_: List of <a href="healthcheckcustomconfig.md">HealthCheckCustomConfig</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### DnsRecords

_Required_: No

_Type_: List of <a href="dnsrecords.md">DnsRecords</a>

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return Values

### Ref

When you pass the logical ID of this resource to the intrinsic `Ref` function, Ref returns the tfcfnid.

### Fn::GetAtt

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

#### tfcfnid

Internal identifier for tracking resource changes. Do not use.

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.
