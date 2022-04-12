#variable "qualys_instance_type" {
#  description = "Qualys scanner EC2 instance type"
#  type        = "string"
#}

variable "service_name" {
  description = "Service name"
  type        = string
}

variable "vpc_id" {
  description = "AWS VPC Id"
  type        = string
}

variable "subnet_id" {
  description = "AWS Subnet Id"
  type        = string
}

variable "qualys_perscode" {
  description = "Perscode for running Qualys"
  type        = string
}

#variable "qualys_ami_id" {
#description = "ami id used by Qualys"
#type        = "string"
#default     = 
#
