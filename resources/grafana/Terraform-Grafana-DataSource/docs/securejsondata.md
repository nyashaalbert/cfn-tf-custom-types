# Terraform::Grafana::DataSource SecureJsonData

## Syntax

To declare this entity in your AWS CloudFormation template, use the following syntax:

### JSON

<pre>
{
    "<a href="#accesskey" title="AccessKey">AccessKey</a>" : <i>String</i>,
    "<a href="#secretkey" title="SecretKey">SecretKey</a>" : <i>String</i>
}
</pre>

### YAML

<pre>
<a href="#accesskey" title="AccessKey">AccessKey</a>: <i>String</i>
<a href="#secretkey" title="SecretKey">SecretKey</a>: <i>String</i>
</pre>

## Properties

#### AccessKey

The access key required
to access the data source.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

#### SecretKey

The secret key required
to access the data source.

_Required_: Yes

_Type_: String

_Update requires_: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
