# Cryptography-with-Hashing-in-Python
This practicum explores cryptographic hashing in Python as a core element of information security. Hashing is a one-way function that converts data into a fixed-length value that cannot be reversed. It covers MD5, SHA-1, and SHA-256 using hashlib, and demonstrates password protection, integrity checking, and salting to strengthen security.

Practicum Objectives (Scientific Objectives)

This practicum is designed to achieve the following objectives:

To understand the fundamental principles of hashing as a one-way cryptographic function for securing data.
To explore the characteristics and differences between hashing algorithms such as MD5, SHA-1, and SHA-256.
To implement data hashing using Python for various security scenarios.
To analyze how small changes in input produce significant changes in output (avalanche effect).
To utilize hashing for file integrity verification as a mechanism for detecting data tampering.
To apply salting techniques to enhance password security against rainbow table and brute-force attacks.
Theoretical Background
1. Hashing in Cryptography

Hashing is the process of transforming input data into a hash value using a deterministic mathematical function. Its key properties include:

Deterministic: The same input always produces the same hash
Irreversible: The original data cannot be reconstructed from the hash
Fixed-length output: The output size is constant regardless of input size
Avalanche effect: A small change in input produces a significantly different hash
2. Hashing Algorithms

Common hashing algorithms include:

MD5 (Message Digest 5)
Produces a 128-bit hash but is considered insecure due to vulnerability to collision attacks.
SHA-1 (Secure Hash Algorithm 1)
Produces a 160-bit hash but is also deprecated for modern security applications.
SHA-256 (Secure Hash Algorithm 256-bit)
Part of the SHA-2 family, widely used and considered secure for modern systems.
3. Data Integrity Verification

Hashing is used to ensure that data remains unchanged during transmission or storage. If the hash value differs, it indicates that the data has been modified.

4. Password Hashing and Salting

In secure systems:

Passwords are not stored in plaintext
Hash values are stored instead of original data
Salt (random data) is added to:
Prevent precomputed attacks (rainbow tables)
Ensure unique hashes even for identical inputs
Practicum Methodology
1. Basic Hashing Implementation

Students implement hashing functions using the SHA-256 algorithm through the hashlib library. This demonstrates how simple input data can be transformed into complex, irreversible hash values.

Scientific value:
Demonstrates core hashing properties, especially irreversibility and the avalanche effect.

2. Hash Comparison (Verification)

Hash comparison is performed by verifying whether a newly generated hash matches a previously stored hash. This simulates real-world authentication systems.

Scientific value:
Illustrates how systems validate data without storing the original input.

3. File Integrity Check

Files are hashed using chunk-based reading to ensure efficiency. Even minor modifications in the file result in significantly different hash values.

Scientific value:
Applied in:

Malware detection
File download verification
Digital forensics
4. Exploration of Hashing Algorithms

Students compare outputs from MD5, SHA-1, and SHA-256 to understand:

Differences in hash length
Relative security strength

Scientific value:
Provides insight into the evolution of cryptographic algorithms in response to security threats.

5. Salted Hashing Implementation (Advanced Security)

Hashing is enhanced with the addition of salt and the use of key derivation functions such as PBKDF2.

Scientific value:
Represents industry-standard practices for:

Secure password storage
Modern authentication systems
Expected Outcomes

After completing this practicum, students are expected to:

Understand the principles of cryptographic hashing
Implement hashing techniques using Python
Analyze hash changes resulting from input modifications
Apply hashing for data integrity verification
Differentiate the security levels of hashing algorithms
Implement salting techniques for enhanced security
Relevance to Industry

This practicum is highly relevant to real-world applications, particularly in:

Authentication systems (login systems)
Secure password storage
Digital forensics and malware analysis
File integrity verification in software distribution
Blockchain and hash-based security systems

The skills developed include:

Cryptographic implementation
Secure coding practices
Data integrity validation
Scientific Conclusion

This practicum demonstrates that hashing is an essential component of modern security systems. By utilizing Python and the hashlib library, hashing processes can be efficiently implemented for various security applications, including authentication and data integrity verification.

The use of strong algorithms such as SHA-256, combined with salting techniques, highlights best practices in cryptography to enhance system resilience against attacks such as brute-force and collision attacks. Therefore, understanding and implementing hashing techniques is a critical foundation for developing secure cryptographic systems.
