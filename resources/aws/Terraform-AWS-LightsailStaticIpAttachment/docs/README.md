# Terraform::AWS::LightsailStaticIpAttachment

Provides a static IP address attachment - relationship between a Lightsail static IP & Lightsail instance.

~> **Note:** Lightsail is currently only supported in a limited number of AWS Regions, please see ["Regions and Availability Zones in Amazon Lightsail"](https://lightsail.aws.amazon.com/ls/docs/overview/article/understanding-regions-and-availability-zones-in-amazon-lightsail) for more details

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::LightsailStaticIpAttachment",
    "Properties" : {
        "<a href="#instancename" title="InstanceName">InstanceName</a>" : <i>String</i>,
        "<a href="#staticipname" title="StaticIpName">StaticIpName</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::LightsailStaticIpAttachment
Properties:
    <a href="#instancename" title="InstanceName">InstanceName</a>: <i>String</i>
    <a href="#staticipname" title="StaticIpName">StaticIpName</a>: <i>String</i>
</pre>

## Properties

#### InstanceName

The name of the Lightsail instance to attach the IP to.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### StaticIpName

The name of the allocated static IP.

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

#### Id

Returns the <code>Id</code> value.

#### IpAddress

Returns the <code>IpAddress</code> value.
