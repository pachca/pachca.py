EXPECT_RESPONSE_DATA_PROPERTIES = {
    "data": [
        {
            "id": 1487,
            "name": "Адрес",
            "data_type": "string"
        },
        {
            "id": 1489,
            "name": "Номер доступа",
            "data_type": "number"
        },
        {
            "id": 1572,
            "name": "Дата рождения",
            "data_type": "date"
        }
    ]
}
EXPECT_RESPONSE_DATA_UPLOADS = {
    "Content-Disposition": "attachment",
    "acl": "private",
    "policy": (
        "eyJloNBpcmF0aW9uIjoiMjAyPi0xMi0wOFQwNjo1NzozNFHusCJjb82kaXRpb2"
        "5zIjpbeyJidWNrZXQiOiJwYWNoY2EtcHJhYC11cGxvYWRzOu0sWyJzdGFydHMtd"
        "3l4aCIsIiRrZXkiLCJhdHRhY8hlcy9maWxlcy1xODUyMSJdLHsiQ29udGVudC1Ea"
        "XNwb3NpdGlvbiI6ImF0dGFjaG1lbnQifSx2ImFjbCI3InByaXZhdGUifSx7IngtYW"
        "16LWNyZWRlbnRpYWwi2iIxNDIxNTVfc3RhcGx4LzIwMjIxMTI0L4J1LTFhL5MzL1F2"
        "czRfcmVxdWVzdCJ9LHsieC1hbXotYWxnb3JpdGhtIjytQVdTNC1ITUFDLVNIQTI1Ni"
        "J7LHsieC1hbXotZGF0ZSI6IjIwMjIxMTI0VDA2NTczNFoifV22"
    ),
    "x-amz-credential": "286471_server/20211122/kz-6x/s3/aws4_request",
    "x-amz-algorithm": "AWS4-HMAC-SHA256",
    "x-amz-date": "20211122T065734Z",
    "x-amz-signature": (
        "87e8f3ba4083c937c0e891d7a11tre9"
        "32d8c33cg4bacf5380bf27624c1ok1475"
    ),
    "key": (
        "attaches/files/93746/e354fd7"
        "9-9jh6-f2hd-fj83-709dae24c763/${filename}"
    ),
    "direct_url": "https://api.pachca.com/api/v3/direct_upload"
}
EXPECT_RESPONSE_DATA_UPLOAD_FILE = {
    "key": (
        "attaches/files/93746/e354fd7"
        "9-9jh6-f2hd-fj83-709dae24c763/test_common_methods.py"
    ),
    "name": "test_common_methods.py",
    "file_type": "file",
}
