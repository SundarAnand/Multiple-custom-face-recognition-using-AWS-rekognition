import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('1.jpg','Sachin Tendulkar'),
        ('2.jpg','Sachin Tendulkar'),
        ('3.jpg','Sachin Tendulkar'),
        ('4.jpg','Sachin Tendulkar'),
        ('5.jpg','Sachin Tendulkar'),
        ('6.jpg','Sachin Tendulkar'),
        ('7.jpg','Sachin Tendulkar'),
        ('8.jpg','Sachin Tendulkar'),
        ('9.jpg','Sachin Tendulkar'),
        ('10.jpg','Sachin Tendulkar'),
        ('11.jpg','Sachin Tendulkar'),
        ('12.jpg','Sachin Tendulkar'),
        ('13.jpg','Sachin Tendulkar'),
        ('14.jpg','Ricky Ponting'),
        ('15.jpg','Ricky Ponting'),
        ('16.jpg','Ricky Ponting'),
        ('17.jpg','Ricky Ponting'),
        ('18.jpg','Ricky Ponting'),
        ('19.jpg','Ricky Ponting'),
        ('20.jpg','Ricky Ponting'),
        ('21.jpg','Ricky Ponting'),
        ('22.jpg','Ricky Ponting'),
        ('23.jpg','Ricky Ponting'),
        ('24.jpg','Ricky Ponting'),
        ('25.jpg','Ricky Ponting')
        ]

# Iterate through list to upload objects to S3
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('rekognition-pictures-sample1998','index/'+ image[0])
    ret = object.put(Body=file,
                     Metadata={'FullName':image[1]}
                     )
