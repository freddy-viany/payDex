from distutils.core import setup
setup(
  name = 'payDex',         
  packages = ['payDex'],   
  version = '0.1',      
  license='MIT',        
  description = 'pay Dex, paiement in cameroun base on payUnit',   
  author = 'fredex',                   
  author_email = 'freddyviany@gmail.com',      
  url = 'https://github.com/freddy-viany/payDex',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/user/reponame/archive/v_01.tar.gz',    # I explain this later on
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second   
          'requests',
          'uuid',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      
    'Intended Audience :: Developers',      
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   
    'Programming Language :: Python :: 3',      
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
  ],
)
