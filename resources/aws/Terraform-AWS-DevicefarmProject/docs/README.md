# Terraform::AWS::DevicefarmProject

Provides a resource to manage AWS Device Farm Projects. 
Please keep in mind that this feature is only supported on the "us-west-2" region.
This resource will error if you try to create a project in another region.

For more information about Device Farm Projects, see the AWS Documentation on
[Device Farm Projects][aws-get-project].

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "Type" : "Terraform::AWS::DevicefarmProject",
    "Properties" : {
        "<a href="#name" title="Name">Name</a>" : <i>String</i>
    }
}
</pre>

### YAML

<pre>
Type: Terraform::AWS::DevicefarmProject
Properties:
    <a href="#name" title="Name">Name</a>: <i>String</i>
</pre>

## Properties

#### Name

The name of the project.

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

#### Arn

Returns the <code>Arn</code> value.

#### Id

Returns the <code>Id</code> value.
