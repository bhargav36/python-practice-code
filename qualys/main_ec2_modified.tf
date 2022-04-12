data "aws_subnet_ids" "subnets" {
  vpc_id = var.vpc_id
}

data "aws_vpc" "vpc" {
  id = var.vpc_id
}

data "aws_region" "current" {
}

data "aws_ami" "qualys" {
  filter {
    name   = "name"
    values = ["qVSA-AWS-2.*.* HVM EBS secure pre-authorized-*"]
  }

  most_recent = true
  owners      = ["679593333241"]
}

resource "aws_instance" "qualys_v_scanner" {
  ami                    = data.aws_ami.qualys.id
  instance_type          = "t2.medium"
  user_data              = "PERSCODE=${var.qualys_perscode}"
  subnet_id              = var.subnet_id
  vpc_security_group_ids = [aws_security_group.qualys_sg.id]

  tags = {
    Name = "${var.service_name} Qualys Virtual Scanner"
  }
}

# create a new security group for qualys and associate with the scanner instance
resource "aws_security_group" "qualys_sg" {
  name        = "${var.service_name}_qualys_sg"
  description = "Security Group for ${var.service_name} VPC qualys virtual scanner"
  vpc_id      = var.vpc_id

  egress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = [data.aws_vpc.vpc.cidr_block]
  }

  tags = {
    Name = "${var.service_name}_qualys_v_scanner_sg"
  }
}

