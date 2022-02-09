provider "aws" {
shared_credentials_file = "/users/tf_user/.aws/creds"
region = ""
profile = "customprofile"
}

resource "aws_instance" "example" {
ami = "" 
instance_type ="t2.micro"
}
