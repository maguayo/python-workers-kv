from distutils.core import setup


setup(
    name = 'python-workers-kv',
    packages = ['WorkersKV'],
    version = '0.2',
    license='MIT',
    description = 'A Cloudflare Workers KV API Wrapper made with Python.',
    author = 'Marcos Aguayo',
    author_email = 'marcos@aguayo.es',
    url = 'https://github.com/maguayo/python-workers-kv',
    download_url = 'https://github.com/maguayo/python-workers-kv/archive/master.zip',
    keywords = ['cloudflare', 'workers', 'kv', 'workers kv'],
    install_requires=['asn1crypto', 'certifi', 'cffi', 'chardet', 'cryptography', 'idna', 'pycparser', 'pyOpenSSL', 'requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
