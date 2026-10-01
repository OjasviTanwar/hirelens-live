# question_bank.py

QUESTION_BANK = {

    # ================= FRONTEND =================
    "frontend": {
        "easy": {
            "theory": [
                {
                    "question": "What is HTML?",
                    "expected_answer": "HTML stands for HyperText Markup Language. It is the standard language used to create and structure content on the web. HTML uses elements represented by tags like headings, paragraphs, links, images, and forms to define the structure of a webpage. It is not a programming language but a markup language that tells the browser how to display content."
                },
                {
                    "question": "What is CSS?",
                    "expected_answer": "CSS stands for Cascading Style Sheets. It controls the visual presentation of HTML elements including layout, colors, fonts, spacing, and animations. CSS separates content from design using selectors to target HTML elements and apply style rules. CSS can be inline, internal using style tags, or external using a separate stylesheet file."
                },
                {
                    "question": "What is JavaScript?",
                    "expected_answer": "JavaScript is a lightweight interpreted programming language used to make webpages interactive and dynamic. It runs in the browser and can manipulate the DOM, handle events, make API calls, and update content without reloading the page. JavaScript supports object-oriented, functional, and event-driven programming paradigms."
                },
                {
                    "question": "Difference between inline and block elements?",
                    "expected_answer": "Block elements like div, p, and h1 take up the full width of their container and start on a new line. Inline elements like span, a, and strong only take up as much width as their content and do not start on a new line. Block elements can contain both block and inline elements while inline elements should only contain other inline elements."
                },
                {
                    "question": "What is the DOM?",
                    "expected_answer": "The DOM stands for Document Object Model. It is a programming interface that represents an HTML document as a tree structure where each node is an object representing part of the document such as elements, attributes, or text. JavaScript uses the DOM to dynamically access, modify, add, or delete HTML elements and their content or styles."
                },
                {
                    "question": "What is responsive design?",
                    "expected_answer": "Responsive design is an approach that makes webpages render well on different screen sizes and devices such as desktops, tablets, and mobile phones. It uses fluid grids, flexible images, and CSS media queries to adapt layout based on screen width. The goal is to provide a good user experience on any device without creating separate websites."
                },
                {
                    "question": "What is a media query?",
                    "expected_answer": "A media query is a CSS technique that applies styles based on device characteristics like screen width, height, or orientation. It uses the @media rule followed by a condition. For example you can apply different font sizes or layouts for screens smaller than 768 pixels. Media queries are the core tool for building responsive designs."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Create a simple responsive navbar.",
                    "expected_answer": "A navbar using HTML and CSS with flexbox for layout and media queries to stack links vertically on smaller screens. Should include a logo or brand name and navigation links.",
                    "eval_type": "manual",
                    "test_cases": []
                },
                {
                    "question": "[CODING] Center a div using CSS.",
                    "expected_answer": "Use flexbox on the parent with display flex, justify-content center, and align-items center. Alternatively use margin auto with a defined width, or CSS Grid with place-items center.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain event bubbling.",
                    "expected_answer": "Event bubbling is a DOM event propagation mechanism where an event triggered on a child element bubbles up through its parent elements all the way to the document root. For example clicking a button inside a div will first trigger the button click handler then the div click handler. You can stop bubbling using event.stopPropagation(). The opposite is event capturing which goes from root down to the target."
                },
                {
                    "question": "What is flexbox?",
                    "expected_answer": "Flexbox is a CSS layout model that provides an efficient way to arrange, align, and distribute space among items in a container. The container uses display flex and properties like flex-direction, justify-content, align-items, and flex-wrap. Child items use flex-grow, flex-shrink, and flex-basis. Flexbox is one-dimensional working on either rows or columns at a time."
                },
                {
                    "question": "What is grid layout?",
                    "expected_answer": "CSS Grid is a two-dimensional layout system that allows creating complex layouts using rows and columns simultaneously. You define a grid container with display grid and use properties like grid-template-columns, grid-template-rows, and gap. Child items can span multiple rows or columns. Grid is more powerful than flexbox for complex two-dimensional layouts."
                },
                {
                    "question": "Difference between var, let, const?",
                    "expected_answer": "Var is function-scoped and hoisted with undefined. Let and const are block-scoped introduced in ES6. Let allows reassignment while const does not allow reassignment after declaration. Var can be re-declared in the same scope but let and const cannot. Const does not mean immutable for objects and arrays since their properties can still be changed."
                },
                {
                    "question": "What is async and await?",
                    "expected_answer": "Async and await are syntactic sugar for working with Promises in JavaScript. An async function always returns a Promise. The await keyword pauses execution inside the async function until the Promise resolves. This allows writing asynchronous code that reads like synchronous code. Error handling is done with try-catch blocks around awaited calls."
                },
                {
                    "question": "Explain closures in JavaScript.",
                    "expected_answer": "A closure is a function that remembers and accesses variables from its outer scope even after the outer function has finished executing. This happens because JavaScript functions maintain a reference to their lexical environment. Closures are used for data privacy, factory functions, and maintaining state. A common example is a counter function that increments a private variable."
                },
                {
                    "question": "What is localStorage?",
                    "expected_answer": "localStorage is a Web Storage API that allows storing key-value pairs in the browser with no expiration date. Data persists even after the browser is closed and can store up to about 5MB per origin. You use localStorage.setItem to store, getItem to retrieve, and removeItem to delete. Unlike cookies it is not sent to the server with every request."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Implement a debounce function.",
                    "expected_answer": "A debounce function takes a function and a delay in milliseconds and returns a new function that delays invoking the original until after the delay has elapsed since the last call. Uses setTimeout and clearTimeout internally.",
                    "eval_type": "manual",
                    "test_cases": []
                },
                {
                    "question": "[CODING] Build a form validation script.",
                    "expected_answer": "Validates form fields such as checking email format with regex, password minimum length, and required fields not being empty. Shows error messages for invalid fields and prevents form submission.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain virtual DOM.",
                    "expected_answer": "The virtual DOM is a lightweight in-memory representation of the real DOM used by React. When state changes React creates a new virtual DOM tree and compares it with the previous one using a diffing algorithm. Only the actual differences are applied to the real DOM in reconciliation. This minimizes expensive real DOM operations and improves performance significantly."
                },
                {
                    "question": "What is reconciliation?",
                    "expected_answer": "Reconciliation is the process React uses to update the real DOM efficiently. When state or props change React builds a new virtual DOM tree and diffs it against the previous one. React uses heuristics like comparing element types and keys to identify what changed. Only the minimal set of changes is applied to the actual DOM making updates fast."
                },
                {
                    "question": "How does React lifecycle work?",
                    "expected_answer": "React components go through mounting, updating, and unmounting phases. In class components lifecycle methods like componentDidMount, componentDidUpdate, and componentWillUnmount handle these phases. In functional components the useEffect hook covers all three phases. Empty dependency array runs after mount, with dependencies runs on updates, and the return function runs on unmount for cleanup."
                },
                {
                    "question": "Explain performance optimization techniques.",
                    "expected_answer": "Key frontend performance techniques include lazy loading images and components, code splitting, memoization using React.memo and useMemo to avoid unnecessary re-renders, debouncing and throttling event handlers, using a CDN for static assets, minimizing DOM manipulation, compressing resources, and using virtualization for long lists with react-window."
                },
                {
                    "question": "What is hydration in frontend?",
                    "expected_answer": "Hydration is the process where a server-side rendered HTML page is made interactive by attaching JavaScript event listeners and React state on the client side. The browser receives pre-rendered HTML which is visible immediately, then React hydrates it by reconciling the server-rendered markup with the client-side component tree making it fully interactive without re-rendering from scratch."
                },
                {
                    "question": "How does event loop work?",
                    "expected_answer": "JavaScript is single-threaded and uses an event loop to handle asynchronous operations. The call stack executes synchronous code. Asynchronous callbacks are placed in the callback queue or microtask queue. The event loop checks if the call stack is empty and pushes callbacks from the queue to the stack. Microtasks like Promise callbacks run before macrotasks like setTimeout."
                },
                {
                    "question": "Explain SSR vs CSR.",
                    "expected_answer": "Server Side Rendering generates full HTML on the server giving faster initial page load and better SEO since content is available immediately. Client Side Rendering sends a minimal HTML shell and renders content in the browser using JavaScript giving slower initial load but faster subsequent navigation. SSR suits content-heavy public pages while CSR suits interactive web applications."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Build a mini todo app with state management.",
                    "expected_answer": "A todo app with an array of tasks in state supporting adding a new task via input, deleting a task by index, and toggling a task as complete or incomplete with state changes re-rendering the list.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        }
    },

    # ================= DATA ANALYTICS =================
    "data_analytics": {
        "easy": {
            "theory": [
                {
                    "question": "What is data analytics?",
                    "expected_answer": "Data analytics is the process of examining raw data to draw conclusions and discover useful insights supporting decision making. There are four types: descriptive which describes what happened, diagnostic which explains why it happened, predictive which forecasts what might happen, and prescriptive which recommends actions to take."
                },
                {
                    "question": "Difference between data analysis and data science?",
                    "expected_answer": "Data analysis focuses on examining existing datasets to answer specific questions using statistical methods and visualization. Data science is broader including building predictive models and machine learning algorithms working with large unstructured datasets. Data analysts use Excel and SQL while data scientists use Python, R, and machine learning frameworks."
                },
                {
                    "question": "What is data cleaning?",
                    "expected_answer": "Data cleaning is identifying and correcting errors, inconsistencies, and inaccuracies in a dataset to improve quality. It includes handling missing values by imputation or removal, removing duplicates, correcting wrong data types, fixing inconsistent formatting, and removing outliers. Clean data is essential because poor quality data leads to inaccurate analysis and unreliable models."
                },
                {
                    "question": "What is descriptive statistics?",
                    "expected_answer": "Descriptive statistics summarizes and describes the main features of a dataset. Measures of central tendency include mean, median, and mode. Measures of spread include variance, standard deviation, and range. Other descriptors include minimum, maximum, and percentiles. Descriptive statistics gives a quick overview of the data distribution without drawing conclusions beyond the data itself."
                },
                {
                    "question": "What is mean and median?",
                    "expected_answer": "Mean is the arithmetic average calculated by summing all values and dividing by count. It is sensitive to outliers. Median is the middle value when data is sorted. For even count it is the average of the two middle values. Median is more robust to outliers. In a salary dataset with one very high earner the median better represents the typical salary than the mean."
                },
                {
                    "question": "What is a dataset?",
                    "expected_answer": "A dataset is a structured collection of related data organized in a table format with rows representing individual records and columns representing variables or features. Datasets can be stored in CSV, Excel, JSON, or databases. They are the fundamental input for data analysis and machine learning and can be labeled for supervised learning or unlabeled for unsupervised learning."
                },
                {
                    "question": "What is visualization?",
                    "expected_answer": "Data visualization is the graphical representation of data using charts, graphs, and maps to communicate patterns, trends, and insights clearly. Common types include bar charts for comparisons, line charts for trends over time, scatter plots for relationships, histograms for distributions, and pie charts for proportions. Good visualization makes complex data accessible and supports faster decision making."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Calculate mean of a list in Python.",
                    "expected_answer": "Sum all values and divide by count, or use statistics.mean() or numpy.mean().",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": [1, 2, 3, 4], "expected": 2.5},
                        {"input": [10, 20],      "expected": 15.0},
                        {"input": [5],            "expected": 5.0}
                    ]
                },
                {
                    "question": "[CODING] Plot a simple bar chart using matplotlib.",
                    "expected_answer": "Use plt.bar() with category labels and values, add axis labels and title, then display with plt.show().",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain hypothesis testing.",
                    "expected_answer": "Hypothesis testing determines if there is enough evidence in a sample to support a claim about a population. The null hypothesis H0 states no effect exists. The alternative hypothesis H1 states there is an effect. We calculate a p-value and compare it against significance level alpha usually 0.05. If p-value is less than alpha we reject the null hypothesis concluding the result is statistically significant."
                },
                {
                    "question": "What is standard deviation?",
                    "expected_answer": "Standard deviation measures the amount of spread in a dataset relative to its mean. A low standard deviation means values are clustered close to the mean while high means values are spread out. It is the square root of variance and is in the same units as the original data making it more interpretable. It is widely used in statistics, finance, and quality control."
                },
                {
                    "question": "What is correlation?",
                    "expected_answer": "Correlation measures the strength and direction of the linear relationship between two variables. The Pearson correlation coefficient ranges from negative one to positive one. Near positive one indicates strong positive relationship, near negative one indicates strong negative relationship, and near zero indicates no linear relationship. Correlation does not imply causation."
                },
                {
                    "question": "What is regression?",
                    "expected_answer": "Regression is a supervised technique to predict a continuous numerical output based on one or more input features. Linear regression fits a line minimizing sum of squared errors. Multiple regression uses multiple features. Polynomial regression handles non-linear relationships. Regression is used for predicting prices, temperatures, and sales figures."
                },
                {
                    "question": "What is EDA?",
                    "expected_answer": "Exploratory Data Analysis analyzes datasets to summarize main characteristics before formal modeling using statistical summaries and visualizations. It helps understand distributions, detect outliers, find patterns, check assumptions, and identify relationships. Techniques include histograms, box plots, scatter plots, correlation matrices, and value counts to guide feature selection and model choice."
                },
                {
                    "question": "Explain A/B testing.",
                    "expected_answer": "A/B testing is a controlled experiment comparing two versions of something to determine which performs better. Users are randomly split into group A seeing the control and group B seeing the variant. Metrics like click-through rate or conversion rate are measured. Statistical significance testing determines if differences are real or due to chance. A/B testing is widely used in product development and marketing."
                },
                {
                    "question": "What is data normalization?",
                    "expected_answer": "Data normalization scales numerical features to a standard range to prevent features with larger magnitudes from dominating the model. Min-max normalization scales values between 0 and 1. Z-score standardization scales to zero mean and unit variance. Normalization is important for distance-based algorithms like K-nearest neighbors and neural networks that are sensitive to feature scales."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Perform train-test split using sklearn.",
                    "expected_answer": "Use train_test_split from sklearn.model_selection with test_size parameter to split data into training and testing sets.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": ([1, 2, 3, 4, 5], 0.2), "expected": None}
                    ]
                },
                {
                    "question": "[CODING] Normalize a numpy array.",
                    "expected_answer": "Subtract minimum value and divide by the range (max minus min) to scale all values between 0 and 1.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": [0, 5, 10], "expected": [0.0, 0.5, 1.0]},
                        {"input": [1, 2, 3],  "expected": [0.0, 0.5, 1.0]}
                    ]
                }
            ]
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain p-value.",
                    "expected_answer": "The p-value is the probability of obtaining results at least as extreme as observed assuming the null hypothesis is true. A small p-value less than 0.05 means the data is unlikely under the null hypothesis so we reject it. A large p-value means data is consistent with the null hypothesis. The p-value does not measure the probability that the null hypothesis is true or the size of an effect."
                },
                {
                    "question": "What is multicollinearity?",
                    "expected_answer": "Multicollinearity occurs when two or more independent variables in a regression model are highly correlated with each other making it difficult to determine individual effects and leading to unstable coefficient estimates. It is detected using the Variance Inflation Factor where VIF above 10 indicates serious multicollinearity. Solutions include removing correlated variables or using regularization like ridge regression."
                },
                {
                    "question": "Explain time series analysis.",
                    "expected_answer": "Time series analysis analyzes data points recorded at successive time points to identify trends, seasonality, and cycles. Components include trend as the long-term direction, seasonality as repeating patterns, and noise as random variation. Methods include moving averages, ARIMA models for forecasting, and decomposition. Applications include stock prediction, demand forecasting, and weather prediction."
                },
                {
                    "question": "What is PCA?",
                    "expected_answer": "Principal Component Analysis is a dimensionality reduction technique that transforms high-dimensional data into fewer dimensions called principal components while retaining most variance. It finds orthogonal axes of maximum variance. The first component explains the most variance. PCA reduces computational cost, removes correlated features, and helps with visualization of high-dimensional data."
                },
                {
                    "question": "What is feature engineering?",
                    "expected_answer": "Feature engineering uses domain knowledge to create, transform, or select input variables to improve model performance. Techniques include creating interaction features, binning continuous variables, encoding categorical variables using one-hot or label encoding, extracting date components, and applying mathematical transformations like log to normalize skewed distributions."
                },
                {
                    "question": "Explain outlier detection methods.",
                    "expected_answer": "Outliers differ significantly from other observations. Detection methods include the IQR method where values below Q1 minus 1.5 times IQR or above Q3 plus 1.5 times IQR are flagged. Z-score method flags points more than three standard deviations from the mean. Visual methods include box plots. Machine learning methods include Isolation Forest and Local Outlier Factor for high-dimensional data."
                },
                {
                    "question": "What is cross-validation?",
                    "expected_answer": "Cross-validation evaluates model performance on unseen data by splitting the dataset into multiple folds. In k-fold cross-validation the data is divided into k subsets. The model trains on k minus one folds and tests on the remaining fold repeating k times. The average score across all folds gives a more reliable estimate of model generalization than a single train-test split."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Perform linear regression using sklearn.",
                    "expected_answer": "Import LinearRegression from sklearn.linear_model, reshape input data, fit the model on training data, and use predict to get outputs.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": ([1, 2, 3], [2, 4, 6]), "expected": None}
                    ]
                }
            ]
        }
    },

    # ================= FULLSTACK =================
    "fullstack": {
        "easy": {
            "theory": [
                {
                    "question": "What is full stack development?",
                    "expected_answer": "Full stack development involves developing both the frontend and backend of a web application. The frontend is what users see built with HTML, CSS, and JavaScript. The backend handles server-side logic, databases, and APIs built with Python, Node.js, or Java. A full stack developer can work across all layers from the user interface to the database."
                },
                {
                    "question": "What is REST API?",
                    "expected_answer": "REST stands for Representational State Transfer. A REST API is an architectural style for designing networked applications using HTTP requests for CRUD operations. It uses GET to retrieve, POST to create, PUT or PATCH to update, and DELETE to remove. REST APIs are stateless and responses are typically in JSON format used for frontend to backend communication."
                },
                {
                    "question": "What is HTTP?",
                    "expected_answer": "HTTP stands for HyperText Transfer Protocol. It is the foundation of data communication on the web defining how messages are formatted between clients and servers. HTTP is stateless and follows a request-response model. HTTPS is the secure version using SSL/TLS encryption. Common status codes include 200 for success, 404 for not found, and 500 for server error."
                },
                {
                    "question": "Difference between GET and POST?",
                    "expected_answer": "GET requests retrieve data with parameters in the URL query string. They are cached, bookmarkable, and have length limitations. POST requests send data in the request body to create or update resources. POST is more secure for sensitive data not visible in the URL. GET is idempotent while POST is not. POST has no size limit and is not cached."
                },
                {
                    "question": "What is JSON?",
                    "expected_answer": "JSON stands for JavaScript Object Notation. It is a lightweight data interchange format easy for humans to read and machines to parse. JSON uses key-value pairs and supports strings, numbers, booleans, arrays, objects, and null. It is the standard format for REST API communication. In Python json.loads parses JSON strings and json.dumps converts objects to JSON."
                },
                {
                    "question": "What is a database?",
                    "expected_answer": "A database is an organized collection of data managed by a Database Management System. Relational databases like MySQL and PostgreSQL store data in tables using SQL. Non-relational databases like MongoDB store data in documents or key-value pairs and are more flexible for unstructured data. Databases provide data persistence, integrity, and efficient retrieval."
                },
                {
                    "question": "What is MVC?",
                    "expected_answer": "MVC stands for Model-View-Controller. It separates an application into three components. The Model manages data and business logic. The View handles presentation. The Controller receives user input, calls the model, and returns the appropriate view. MVC improves code organization, maintainability, and makes testing easier by separating concerns clearly."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Create a simple Flask API.",
                    "expected_answer": "A Flask app with at least one route decorated with @app.route that returns a JSON response using jsonify.",
                    "eval_type": "keyword",
                    "keywords": ["flask", "app.route"],
                    "test_cases": []
                },
                {
                    "question": "[CODING] Connect frontend to backend using fetch.",
                    "expected_answer": "Use the fetch API to make a GET or POST request to a backend endpoint, handle the Promise with async await, and parse the JSON response.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain authentication vs authorization.",
                    "expected_answer": "Authentication verifies who a user is by confirming their identity through credentials like username and password. Authorization verifies what an authenticated user is allowed to do by controlling access to resources. Authentication comes first then authorization. Logging in is authentication while checking if a user has admin privileges to delete a record is authorization."
                },
                {
                    "question": "What is JWT?",
                    "expected_answer": "JWT stands for JSON Web Token. It is a compact self-contained token for securely transmitting information. A JWT has three parts: the header containing the algorithm, the payload containing claims like user ID and expiry, and the signature for verification. The server generates a JWT on login and the client sends it with each request in the Authorization header making it stateless."
                },
                {
                    "question": "What is middleware?",
                    "expected_answer": "Middleware sits between the request and response in a web application's processing pipeline intercepting requests to perform tasks like authentication, logging, input validation, error handling, or adding CORS headers before passing control to the route handler. In Flask middleware uses before_request and after_request hooks. Middleware promotes separation of concerns and code reuse."
                },
                {
                    "question": "Explain session management.",
                    "expected_answer": "Session management maintains state for a user across multiple HTTP requests since HTTP is stateless. Server-side sessions store data on the server and send a session ID cookie to the client. Token-based sessions using JWT store all data in a signed token on the client. Secure session management requires HTTPS, secure cookie flags, and implementing session expiry and invalidation on logout."
                },
                {
                    "question": "What is CORS?",
                    "expected_answer": "CORS stands for Cross-Origin Resource Sharing. It is a browser security mechanism restricting web pages from making requests to a different domain. When a frontend calls an API on another domain the browser sends a preflight OPTIONS request. The server must respond with appropriate Access-Control-Allow-Origin headers to grant permission. In Flask the flask-cors extension handles CORS configuration."
                },
                {
                    "question": "Explain microservices.",
                    "expected_answer": "Microservices is an architectural style where an application is built as independent services each responsible for a specific business function. Each service has its own database and communicates via APIs or message queues. Benefits include independent deployment, scalability of individual services, and technology flexibility. Challenges include increased deployment complexity and distributed system debugging."
                },
                {
                    "question": "What is API rate limiting?",
                    "expected_answer": "API rate limiting restricts the number of requests a client can make within a given time window to prevent abuse and server overloading. Common strategies include fixed window, sliding window, and token bucket. When the limit is exceeded the server returns 429 Too Many Requests. Rate limiting can be implemented using Redis to track request counts per client IP or API key."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Implement JWT authentication.",
                    "expected_answer": "Use PyJWT to encode a payload with user ID and expiry into a token on login and decode and verify the token on protected routes.",
                    "eval_type": "keyword",
                    "keywords": ["jwt", "token", "encode", "decode"],
                    "test_cases": []
                },
                {
                    "question": "[CODING] Create CRUD API endpoints.",
                    "expected_answer": "Flask routes implementing GET to retrieve records, POST to create, PUT to update, and DELETE to remove a resource returning appropriate status codes.",
                    "eval_type": "keyword",
                    "keywords": ["app.route", "get", "post", "put", "delete"],
                    "test_cases": []
                }
            ]
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain scalability strategies.",
                    "expected_answer": "Scalability strategies include vertical scaling adding more resources to one server and horizontal scaling adding more servers. Caching with Redis reduces database load. Database sharding partitions data across multiple databases. Asynchronous processing with message queues offloads heavy tasks. CDNs distribute static assets globally. Microservices allow scaling individual components independently based on demand."
                },
                {
                    "question": "What is load balancing?",
                    "expected_answer": "Load balancing distributes incoming traffic across multiple servers to prevent any single server from being overwhelmed improving availability and responsiveness. Algorithms include round robin which distributes equally, least connections which routes to the server with fewest connections, and IP hash which routes the same client to the same server. Load balancers like Nginx also perform health checks removing failed servers from rotation."
                },
                {
                    "question": "Explain Docker basics.",
                    "expected_answer": "Docker is a containerization platform that packages applications and their dependencies into lightweight portable containers. A Dockerfile defines the image with instructions like FROM, RUN, COPY, and CMD. Images are built using docker build and run as containers using docker run. Containers are isolated from each other and the host. Docker Compose orchestrates multi-container applications ensuring consistency across environments."
                },
                {
                    "question": "What is CI/CD?",
                    "expected_answer": "CI/CD stands for Continuous Integration and Continuous Deployment. Continuous Integration automatically builds and tests code every time a developer pushes changes catching bugs early. Continuous Deployment automatically deploys tested code to production after passing all checks. Tools include Jenkins, GitHub Actions, and GitLab CI. CI/CD reduces manual deployment effort and speeds up release cycles."
                },
                {
                    "question": "Explain caching mechanisms.",
                    "expected_answer": "Caching stores frequently accessed data in fast storage to reduce latency and database load. Browser caching stores static assets locally. CDN caching stores assets at edge servers close to users. Server-side caching using Redis stores query results in memory. Cache invalidation strategies include TTL expiry, write-through updating cache and database together, and cache-aside loading data on first miss."
                },
                {
                    "question": "What is reverse proxy?",
                    "expected_answer": "A reverse proxy sits in front of backend servers and forwards client requests to them hiding backend details. Benefits include load balancing, SSL termination, caching, compression, and security by filtering requests. Nginx and Apache are commonly used. In a typical setup Nginx handles static files and proxies API requests to a Flask or Node.js server running on a different port."
                },
                {
                    "question": "Explain distributed systems basics.",
                    "expected_answer": "A distributed system is a collection of independent computers appearing as a single system. The CAP theorem states a distributed system can guarantee only two of consistency, availability, and partition tolerance. Consistency ensures all nodes see the same data. Availability ensures the system responds. Partition tolerance handles network failures. Distributed systems use consensus algorithms like Raft for coordination and face challenges of network latency and partial failures."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Design a scalable REST architecture.",
                    "expected_answer": "A Flask app using Blueprints to modularize routes, middleware for authentication, centralized error handling, and structured project layout separating routes, models, and services.",
                    "eval_type": "keyword",
                    "keywords": ["blueprint", "app.route", "middleware"],
                    "test_cases": []
                }
            ]
        }
    },

    # ================= AIML =================
    "aiml": {
        "easy": {
            "theory": [
                {
                    "question": "What is supervised learning?",
                    "expected_answer": "Supervised learning trains a model on labeled data where each example has an input and a correct output. The model learns to map inputs to outputs by minimizing error between predictions and actual labels. After training it predicts outputs for new unseen inputs. Examples include email spam classification, house price prediction, and image recognition."
                },
                {
                    "question": "Classification vs regression?",
                    "expected_answer": "Classification predicts a discrete category such as spam or not spam. Regression predicts a continuous numerical value such as house price. Classification uses logistic regression, decision trees, and SVM. Regression uses linear and polynomial regression. Evaluation metrics differ: accuracy and F1 for classification, MSE and R-squared for regression."
                },
                {
                    "question": "What is overfitting?",
                    "expected_answer": "Overfitting occurs when a model learns training data too well including noise, resulting in poor performance on new unseen data. An overfit model has high training accuracy but low test accuracy. Prevention techniques include using more training data, simplifying the model, applying regularization, using dropout in neural networks, and cross-validation to detect overfitting early."
                },
                {
                    "question": "Explain bias variance.",
                    "expected_answer": "Bias is error from wrong assumptions causing the model to miss relevant relationships leading to underfitting. Variance is error from sensitivity to training data fluctuations causing the model to model noise leading to overfitting. The bias-variance tradeoff means decreasing bias typically increases variance. The goal is to find a model with low bias and low variance minimizing total prediction error."
                },
                {
                    "question": "Precision vs recall?",
                    "expected_answer": "Precision is true positives divided by true positives plus false positives representing how many positive predictions were correct. Recall is true positives divided by true positives plus false negatives representing how many actual positives were found. High precision minimizes false positives while high recall minimizes false negatives. The F1 score is the harmonic mean balancing both metrics."
                },
                {
                    "question": "What is gradient descent?",
                    "expected_answer": "Gradient descent is an optimization algorithm that minimizes a loss function by iteratively updating parameters in the direction of the negative gradient. The learning rate controls step size. Batch gradient descent uses all training examples, stochastic uses one example at a time, and mini-batch uses small batches. Variants like Adam and RMSprop adapt the learning rate for faster convergence."
                },
                {
                    "question": "What is loss function?",
                    "expected_answer": "A loss function measures how wrong model predictions are compared to actual values quantifying error for training examples. Common loss functions include mean squared error for regression, binary cross-entropy for binary classification, and categorical cross-entropy for multi-class classification. The optimization algorithm minimizes the loss by adjusting model weights during training."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Train test split.",
                    "expected_answer": "Use train_test_split from sklearn.model_selection to split data into training and testing subsets with a specified test size ratio.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": ([1, 2, 3, 4, 5], 0.2), "expected": None}
                    ]
                },
                {
                    "question": "[CODING] Normalize numpy array.",
                    "expected_answer": "Apply min-max normalization by subtracting the minimum value and dividing by the range to scale all values between 0 and 1.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": [0, 5, 10], "expected": [0.0, 0.5, 1.0]},
                        {"input": [1, 2, 3],  "expected": [0.0, 0.5, 1.0]}
                    ]
                }
            ]
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain neural networks.",
                    "expected_answer": "A neural network consists of layers of interconnected neurons. The input layer receives features, hidden layers learn representations through weighted connections and activation functions, and the output layer produces predictions. During training weights are adjusted using backpropagation and gradient descent to minimize the loss function. Deep networks with many hidden layers are called deep learning models."
                },
                {
                    "question": "What is activation function?",
                    "expected_answer": "An activation function introduces non-linearity into a neural network allowing it to learn complex patterns. Without activation functions networks would only compute linear transformations. ReLU returns max of zero and input and is most widely used. Sigmoid squashes output between 0 and 1 for binary output. Softmax converts outputs to probabilities for multi-class classification. Tanh outputs between negative one and one."
                },
                {
                    "question": "What is regularization?",
                    "expected_answer": "Regularization prevents overfitting by adding a penalty to the loss function that discourages complex models. L1 adds the sum of absolute weight values encouraging sparsity by driving some weights to zero. L2 adds sum of squared weights shrinking weights toward zero. Dropout randomly deactivates neurons during training. Regularization improves model generalization to unseen data."
                },
                {
                    "question": "Explain L1 vs L2.",
                    "expected_answer": "L1 regularization called Lasso adds the sum of absolute values of weights to the loss promoting sparsity by driving irrelevant weights to exactly zero performing feature selection. L2 called Ridge adds sum of squared weights shrinking all weights but rarely to zero. L1 is preferred for sparse models with few relevant features. L2 is preferred when all features may be relevant and you want balanced small weights."
                },
                {
                    "question": "What is cross entropy?",
                    "expected_answer": "Cross-entropy is a loss function for classification measuring the difference between predicted probabilities and actual class labels. Binary cross-entropy is used for two-class problems and categorical cross-entropy for multiple classes. It penalizes confident wrong predictions heavily. Lower cross-entropy means predicted probabilities are closer to the true distribution. It is computed as the negative log likelihood of the correct class."
                },
                {
                    "question": "What is confusion matrix?",
                    "expected_answer": "A confusion matrix summarizes classification model performance showing counts of true positives, true negatives, false positives, and false negatives. True positives are correctly predicted positives, true negatives correctly predicted negatives, false positives are negatives predicted as positive, and false negatives are positives predicted as negative. From it we derive accuracy, precision, recall, and F1 score."
                },
                {
                    "question": "What is K-means?",
                    "expected_answer": "K-means is an unsupervised clustering algorithm partitioning data into K clusters. It randomly initializes K centroids then assigns each point to the nearest centroid using Euclidean distance, then recalculates centroids as the mean of assigned points repeating until convergence. K must be specified in advance. The elbow method helps choose K by plotting inertia against K values."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Linear regression using sklearn.",
                    "expected_answer": "Import LinearRegression from sklearn.linear_model, fit the model on input and output data, and use predict to generate outputs.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": ([1, 2, 3], [2, 4, 6]), "expected": None}
                    ]
                },
                {
                    "question": "[CODING] Logistic regression implementation.",
                    "expected_answer": "Import LogisticRegression from sklearn.linear_model, fit on training data with binary labels, and use predict or predict_proba for classification.",
                    "eval_type": "keyword",
                    "keywords": ["logisticregression", "fit", "predict"],
                    "test_cases": []
                }
            ]
        },
        "hard": {
            "theory": [
                {
                    "question": "What is decision tree?",
                    "expected_answer": "A decision tree splits data into subsets based on feature values using a tree structure. Each internal node represents a feature test, each branch represents an outcome, and each leaf represents a class label. Splits maximize information gain or minimize Gini impurity. Decision trees are interpretable but prone to overfitting. Pruning reduces overfitting by removing branches with little predictive power."
                },
                {
                    "question": "Explain random forest.",
                    "expected_answer": "Random forest builds multiple decision trees during training and combines predictions through majority voting for classification or averaging for regression. Each tree trains on a random bootstrap sample using a random subset of features at each split. This diversity among trees reduces variance and overfitting. Random forests handle high-dimensional data well and provide feature importance scores."
                },
                {
                    "question": "What is SVM?",
                    "expected_answer": "Support Vector Machine finds the optimal hyperplane that maximally separates classes with the largest margin. Support vectors are the closest data points to the hyperplane. The kernel trick handles non-linearly separable data by mapping to a higher-dimensional space. Common kernels include linear, polynomial, and RBF. SVM works well for high-dimensional data and small datasets but is slow on large datasets."
                },
                {
                    "question": "What is PCA?",
                    "expected_answer": "Principal Component Analysis transforms data into a new coordinate system where axes are principal components ordered by variance explained. It computes eigenvectors of the covariance matrix. The first component captures the most variance. PCA reduces noise, removes correlated features, and speeds up training. Information loss occurs as components are dropped but the most important structure is preserved."
                },
                {
                    "question": "What is backpropagation?",
                    "expected_answer": "Backpropagation computes gradients of the loss function with respect to each weight using the chain rule of calculus to train neural networks. It works in two passes: the forward pass computes predictions and loss, then the backward pass propagates the error gradient backward through the network layer by layer. Weights are updated by subtracting the gradient multiplied by the learning rate."
                },
                {
                    "question": "What is reinforcement learning?",
                    "expected_answer": "Reinforcement learning trains an agent to make decisions by interacting with an environment to maximize cumulative reward. The agent takes actions in states and receives rewards or penalties. Key concepts include the policy defining action selection, the value function estimating expected future reward, and the Q-function. Algorithms include Q-learning and Deep Q-Networks. Applications include game playing, robotics, and recommendation systems."
                },
                {
                    "question": "Explain hyperparameter tuning.",
                    "expected_answer": "Hyperparameters are model configuration settings like learning rate, number of trees, or regularization strength that are set before training and not learned from data. Grid search exhaustively tries all parameter combinations. Random search samples randomly and is more efficient. Bayesian optimization intelligently chooses next parameters based on past results. Cross-validation evaluates each combination avoiding overfitting to the test set."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Implement K-means from scratch.",
                    "expected_answer": "Initialize K centroids randomly, assign each point to the nearest centroid using Euclidean distance, update centroids as the mean of assigned points, and repeat until convergence.",
                    "eval_type": "keyword",
                    "keywords": ["centroid", "cluster", "kmeans", "distance"],
                    "test_cases": []
                }
            ]
        }
    },

    # ================= DSA =================
    "dsa": {
        "easy": {
            "theory": [
                {
                    "question": "What is an array?",
                    "expected_answer": "An array is a linear data structure storing elements of the same type in contiguous memory locations. Each element is accessed using an index starting from zero. Arrays have O(1) random access, O(n) search for unsorted arrays, and O(n) insertion or deletion in the middle since elements must shift. Dynamic arrays like Python lists can resize automatically."
                },
                {
                    "question": "What is a linked list?",
                    "expected_answer": "A linked list stores elements called nodes non-contiguously where each node contains data and a pointer to the next node. Linked lists have O(1) insertion and deletion at the head but O(n) access by index. A singly linked list has next pointers only, doubly linked has both next and previous, and circular connects the tail back to the head."
                },
                {
                    "question": "What is a stack?",
                    "expected_answer": "A stack is a linear data structure following Last In First Out principle. Elements are added and removed from the same end called the top. Operations are push to add, pop to remove, and peek to view without removing. Stacks are used for function call management in recursion, undo operations, expression evaluation, and depth-first search."
                },
                {
                    "question": "What is a queue?",
                    "expected_answer": "A queue follows First In First Out principle where elements are added at the rear and removed from the front. Operations are enqueue to add and dequeue to remove. Queues are used in breadth-first search, CPU scheduling, print spooling, and message buffering. Variants include priority queue and deque allowing insertion and deletion from both ends."
                },
                {
                    "question": "What is time complexity?",
                    "expected_answer": "Time complexity describes how the runtime of an algorithm grows as input size increases expressed using Big-O notation representing worst case. Common complexities are O(1) constant, O(log n) logarithmic, O(n) linear, O(n log n) linearithmic, O(n squared) quadratic, and O(2 to the n) exponential. Time complexity helps compare algorithms and choose the most efficient solution."
                },
                {
                    "question": "What is Big-O notation?",
                    "expected_answer": "Big-O notation describes the upper bound of an algorithm's time or space complexity in terms of input size n representing the worst-case growth rate ignoring constants and lower-order terms. For example an algorithm taking 3n squared plus 2n steps has O(n squared). It allows comparing algorithms independently of hardware. Common classes are O(1), O(log n), O(n), O(n log n), O(n squared), and O(2 to the n)."
                },
                {
                    "question": "Difference between linear and binary search?",
                    "expected_answer": "Linear search checks each element one by one from the beginning until the target is found working on unsorted data with O(n) time complexity. Binary search repeatedly divides a sorted array in half comparing the target with the middle element narrowing the search to left or right half. Binary search has O(log n) time complexity but requires sorted data."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Find maximum in a list.",
                    "expected_answer": "Iterate through the list tracking the largest value seen so far, or use Python's built-in max() function.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": [1, 5, 3],    "expected": 5},
                        {"input": [-1, -5, -2], "expected": -1},
                        {"input": [100],         "expected": 100}
                    ]
                },
                {
                    "question": "[CODING] Check if string is palindrome.",
                    "expected_answer": "Compare the string with its reverse using s == s[::-1], or use two pointers from both ends moving inward checking equality.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": "madam",   "expected": True},
                        {"input": "hello",   "expected": False},
                        {"input": "racecar", "expected": True},
                        {"input": "world",   "expected": False}
                    ]
                }
            ]
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain recursion.",
                    "expected_answer": "Recursion is a technique where a function calls itself to solve smaller instances of the same problem. Every recursive function needs a base case that stops the recursion and a recursive case breaking the problem into smaller subproblems. Recursion uses the call stack to store intermediate states. Examples include factorial, Fibonacci, tree traversal, and merge sort."
                },
                {
                    "question": "What is a binary tree?",
                    "expected_answer": "A binary tree is a hierarchical data structure where each node has at most two children called left and right. A binary search tree has left subtree with smaller values and right with larger enabling O(log n) search. Traversals include inorder giving sorted output, preorder, and postorder. Binary trees are used in expression parsing and database indexing."
                },
                {
                    "question": "What is a hash table?",
                    "expected_answer": "A hash table maps keys to values using a hash function to compute an index into an array of buckets providing O(1) average time for insertion, deletion, and lookup. Collisions are resolved using chaining storing a linked list at each bucket or open addressing probing for another empty slot. Python dictionaries are implemented as hash tables."
                },
                {
                    "question": "Explain merge sort.",
                    "expected_answer": "Merge sort divides the array into two halves recursively until each subarray has one element then merges sorted subarrays back together comparing elements from both halves. Merge sort has O(n log n) time complexity in all cases making it predictably efficient. It requires O(n) extra space and is stable maintaining relative order of equal elements."
                },
                {
                    "question": "Explain quick sort.",
                    "expected_answer": "Quick sort selects a pivot element and partitions the array into elements less than and greater than the pivot then recursively sorts both partitions. Average case is O(n log n) but worst case is O(n squared) with a bad pivot. Random pivot selection reduces worst case risk. Quick sort is in-place requiring O(log n) stack space and is cache-friendly making it fast in practice."
                },
                {
                    "question": "What is dynamic programming?",
                    "expected_answer": "Dynamic programming solves complex problems by breaking them into overlapping subproblems solving each once and storing results to avoid redundant computation. Top-down with memoization caches recursive results. Bottom-up tabulation builds iteratively from base cases. It applies when a problem has optimal substructure and overlapping subproblems. Classic examples include knapsack and longest common subsequence."
                },
                {
                    "question": "What is graph traversal?",
                    "expected_answer": "Graph traversal visits all nodes systematically. Breadth-first search uses a queue visiting all neighbors before going deeper exploring level by level and finding shortest paths in unweighted graphs. Depth-first search uses a stack or recursion exploring as far as possible before backtracking and is used for cycle detection and topological sorting. Both have O(V plus E) time complexity."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Implement binary search.",
                    "expected_answer": "Maintain low and high pointers, compute mid index, compare target with mid element, and narrow the search to left or right half until found or pointers cross.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": ([1, 2, 3, 4, 5], 4),  "expected": 3},
                        {"input": ([10, 20, 30], 10),     "expected": 0},
                        {"input": ([5, 10, 15, 20], 15),  "expected": 2}
                    ]
                },
                {
                    "question": "[CODING] Reverse a linked list.",
                    "expected_answer": "Use three pointers prev initialized to None, curr to head, and next. At each step store next, point curr.next to prev, move prev to curr, and curr to next.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": [1, 2, 3], "expected": [3, 2, 1]},
                        {"input": [4, 5],    "expected": [5, 4]},
                        {"input": [7],       "expected": [7]}
                    ]
                }
            ]
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain AVL trees.",
                    "expected_answer": "An AVL tree is a self-balancing binary search tree where left and right subtree heights of every node differ by at most one. Balance is maintained through rotations: single left, single right, left-right, and right-left performed after insertions or deletions that violate the balance property. AVL trees guarantee O(log n) search, insertion, and deletion in the worst case."
                },
                {
                    "question": "What is a red-black tree?",
                    "expected_answer": "A red-black tree is a self-balancing BST where each node is colored red or black. Rules are: the root is black, red nodes cannot have red children, and every path from root to null has the same number of black nodes. These ensure height O(log n) giving O(log n) worst-case operations. Used in Java TreeMap, C++ STL map, and the Linux kernel scheduler."
                },
                {
                    "question": "Explain Dijkstra's algorithm.",
                    "expected_answer": "Dijkstra's algorithm finds shortest paths from a source node to all other nodes in a weighted graph with non-negative edges. It uses a priority queue to greedily select the unvisited node with smallest known distance then updates distances to neighbors. Time complexity is O(V squared) with adjacency matrix or O(E log V) with a binary heap. It does not work with negative edge weights."
                },
                {
                    "question": "What is topological sorting?",
                    "expected_answer": "Topological sorting produces a linear ordering of vertices in a directed acyclic graph where for every edge from u to v, u appears before v. Only possible in DAGs. Kahn's algorithm uses in-degree counting and a queue. DFS-based topological sort adds nodes to a stack after all neighbors are visited. Applications include task scheduling, build systems, and course prerequisite ordering."
                },
                {
                    "question": "Explain knapsack problem.",
                    "expected_answer": "The knapsack problem maximizes total value of items placed in a knapsack with limited weight capacity. The 0/1 knapsack allows each item to be taken or left solved with dynamic programming in O(n times W) time. The fractional knapsack allows taking fractions solved greedily by sorting by value-to-weight ratio. Applications include resource allocation and portfolio selection."
                },
                {
                    "question": "Explain Floyd-Warshall algorithm.",
                    "expected_answer": "Floyd-Warshall finds shortest paths between all pairs of vertices including negative edge weights but not negative cycles using dynamic programming. The recurrence is dist[i][j] equals minimum of dist[i][j] and dist[i][k] plus dist[k][j] for each intermediate vertex k. Time complexity is O(V cubed) and space is O(V squared). It detects negative cycles when dist[i][i] becomes negative."
                },
                {
                    "question": "What is amortized analysis?",
                    "expected_answer": "Amortized analysis calculates the average time per operation over a sequence of operations even if some individual operations are expensive giving a more accurate performance measure. The aggregate method divides total cost by operations. The accounting method assigns credits to cheap operations to pay for expensive ones later. A classic example is dynamic array resizing where occasional O(n) copies amortize to O(1) per push."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Implement LRU cache.",
                    "expected_answer": "Use an OrderedDict to maintain insertion order. On get move the accessed key to the end. On put insert the key and if capacity is exceeded remove the first item which is the least recently used.",
                    "eval_type": "auto",
                    "test_cases": [
                        {"input": (2,), "expected": None}
                    ]
                }
            ]
        }
    },

    # ================= PERSONAL / HR =================
    "personal": {
        "easy": {
            "theory": [
                {
                    "question": "Tell me about yourself.",
                    "expected_answer": "A strong answer covers four things: who you are, your educational background, your key technical skills, and why you are interested in this role. It should be 60 to 90 seconds long, structured, and end with why you are excited about the opportunity. Avoid reciting your resume and instead highlight what makes you relevant for the position."
                },
                {
                    "question": "What are your strengths?",
                    "expected_answer": "Mention two or three genuine strengths that are relevant to the job such as problem solving, quick learning, or teamwork. Back each strength with a specific example. For instance if you say you are a quick learner explain how you picked up a new technology for a project. Avoid generic answers like hardworking without supporting evidence."
                },
                {
                    "question": "What are your weaknesses?",
                    "expected_answer": "Choose a real weakness that is not a core requirement of the job and show what you are doing to improve it. For example say you sometimes spend too much time perfecting code but you have started setting time limits for tasks. This shows self-awareness and a growth mindset. Never say you have no weaknesses."
                },
                {
                    "question": "Why do you want to work here?",
                    "expected_answer": "Show that you have researched the company. Mention specific things about their products, culture, or mission that genuinely appeal to you. Connect your skills and career goals to what the company does. Avoid saying it is only for the salary or because it is a good company without specifics."
                },
                {
                    "question": "Where do you see yourself in 5 years?",
                    "expected_answer": "Show ambition while staying realistic and relevant to the company. Mention that you want to grow your technical skills, take on more responsibility, and contribute to meaningful projects. Align your goals with what the company offers. Avoid saying you want to start your own company or be in a completely different field."
                },
                {
                    "question": "Why should we hire you?",
                    "expected_answer": "Summarize your top three relevant skills or qualities and connect them directly to the job requirements. Show enthusiasm for the role. Give a concrete example of a problem you solved or a project you delivered. End with confidence by saying you are ready to contribute immediately and are eager to grow with the team."
                },
                {
                    "question": "Tell me about a challenge you faced and how you overcame it.",
                    "expected_answer": "Use the STAR method: describe the Situation, the Task you needed to complete, the Action you took, and the Result. Choose a real technical or team challenge. Focus more on your actions and the positive outcome than on the problem itself. Show problem-solving ability, resilience, and what you learned from the experience."
                }
            ],
            "coding": []
        },
        "medium": {
            "theory": [
                {
                    "question": "Describe a time you worked in a team.",
                    "expected_answer": "Use the STAR method to describe a specific team project. Explain your role, how you communicated and collaborated with team members, how you handled disagreements, and what the outcome was. Highlight your contribution without taking all the credit. Show that you value teamwork, listen to others, and can resolve conflicts constructively."
                },
                {
                    "question": "How do you handle pressure and tight deadlines?",
                    "expected_answer": "Describe your approach to prioritization such as breaking tasks into smaller pieces, focusing on high-impact items first, and communicating early if you are behind. Give a real example of a deadline you met under pressure. Show that you stay calm, think clearly, and do not compromise quality under stress."
                },
                {
                    "question": "What motivates you?",
                    "expected_answer": "Talk about intrinsic motivators that are relevant to the work such as solving complex problems, learning new technologies, seeing your work make a real impact, or helping teammates succeed. Be genuine and specific. Avoid saying money or job security as your primary motivator in a technical interview setting."
                },
                {
                    "question": "How do you handle criticism or negative feedback?",
                    "expected_answer": "Say that you welcome constructive feedback because it helps you improve. Describe a situation where you received criticism, how you listened without becoming defensive, what you changed as a result, and the positive outcome. Show emotional maturity, openness to learning, and the ability to separate personal feelings from professional growth."
                },
                {
                    "question": "Tell me about a time you failed.",
                    "expected_answer": "Choose a genuine failure that is not catastrophic and show what you learned from it. Use the STAR method. Be honest about what went wrong, take responsibility without blaming others, explain what you would do differently now, and show how you applied that learning in a subsequent situation. Growth mindset is the key message."
                },
                {
                    "question": "What are your career goals?",
                    "expected_answer": "Share short-term goals such as mastering specific technologies or contributing to real projects, and long-term goals such as becoming a senior engineer or technical lead. Connect your goals to the company's growth opportunities. Show that you have thought about your career path and that this role fits into your plan genuinely."
                },
                {
                    "question": "How do you prioritize tasks when you have multiple deadlines?",
                    "expected_answer": "Describe a systematic approach such as listing all tasks, estimating time and impact, tackling high priority items first, and communicating proactively about delays. Mention tools or techniques you use like to-do lists, time blocking, or Agile sprint planning. Give an example of managing multiple priorities successfully."
                }
            ],
            "coding": []
        },
        "hard": {
            "theory": [
                {
                    "question": "Describe a situation where you showed leadership.",
                    "expected_answer": "Use STAR to describe a time you took initiative, guided a team, or drove a project without necessarily having a formal leadership title. Explain how you motivated others, made decisions, resolved conflicts, and delivered results. Show that you can lead by example, communicate a clear vision, and take responsibility for outcomes."
                },
                {
                    "question": "How do you handle disagreements with a team member?",
                    "expected_answer": "Describe your approach to resolving conflict professionally such as having a calm one-on-one conversation, actively listening to understand their perspective, finding common ground, and focusing on the best solution for the project rather than winning the argument. Give a real example if possible. Show maturity, empathy, and collaborative problem-solving."
                },
                {
                    "question": "Tell me about a time you went above and beyond.",
                    "expected_answer": "Describe a specific situation where you did more than what was expected such as staying late to fix a critical bug, learning a new skill to help your team, or taking on extra responsibility during a crunch period. Explain why you chose to go the extra mile and what the positive impact was. Show initiative, ownership, and dedication."
                },
                {
                    "question": "How do you stay updated with new technologies?",
                    "expected_answer": "Mention specific resources you use such as reading documentation, following tech blogs, watching conference talks, building side projects, contributing to open source, or taking online courses. Show that learning is a habit for you and give a recent example of something new you learned and applied. Passion for continuous learning is the key message."
                },
                {
                    "question": "What is your biggest professional achievement?",
                    "expected_answer": "Choose an achievement that is relevant to the role such as a project you built, a problem you solved, or an improvement you drove. Quantify the impact where possible such as reduced loading time by 40 percent or led a team of 4. Use STAR to structure your answer. Show pride in your work while remaining humble and team-oriented."
                },
                {
                    "question": "How would your teammates describe you?",
                    "expected_answer": "Mention two or three positive qualities that your teammates would genuinely say such as reliable, a good communicator, always willing to help, or someone who keeps calm under pressure. Back each quality with a brief example or context. Be authentic rather than listing generic traits. This question tests your self-awareness and how you relate to others."
                },
                {
                    "question": "Why are you leaving your current position or why did you choose this field?",
                    "expected_answer": "If switching jobs focus on growth opportunities, new challenges, or better alignment with your goals rather than complaining about your current employer. If a fresher explain why you chose computer science or this specific field such as passion for problem solving, interest in building products, or inspiration from a project. Show positivity and forward-thinking."
                }
            ],
            "coding": []
        }
    },

    # ================= DBMS =================
    "dbms": {
        "easy": {
            "theory": [
                {
                    "question": "What is a DBMS?",
                    "expected_answer": "A Database Management System is software that manages databases allowing users to store, retrieve, update, and delete data efficiently. It provides an interface between users and the database handling data organization, security, concurrency, and backup. Examples include MySQL, PostgreSQL, Oracle, and SQLite."
                },
                {
                    "question": "What is a primary key?",
                    "expected_answer": "A primary key is a column or set of columns that uniquely identifies each row in a table. It cannot contain null values and must be unique for every record. Each table can have only one primary key. Primary keys are used to establish relationships between tables through foreign keys."
                },
                {
                    "question": "What is a foreign key?",
                    "expected_answer": "A foreign key is a column in one table that references the primary key of another table establishing a relationship between them. It enforces referential integrity ensuring that a value in the foreign key column must exist in the referenced table. Foreign keys are fundamental to relational database design."
                },
                {
                    "question": "What is SQL?",
                    "expected_answer": "SQL stands for Structured Query Language. It is the standard language for managing and querying relational databases. SQL commands are categorized as DDL for creating and modifying structures, DML for manipulating data, DCL for access control, and TCL for transaction management. SELECT, INSERT, UPDATE, and DELETE are the most common commands."
                },
                {
                    "question": "What is normalization?",
                    "expected_answer": "Normalization is the process of organizing a database to reduce redundancy and improve data integrity by dividing large tables into smaller related ones. Normal forms include 1NF which eliminates repeating groups, 2NF which removes partial dependencies, and 3NF which removes transitive dependencies. Higher normal forms further reduce anomalies."
                },
                {
                    "question": "What is a join in SQL?",
                    "expected_answer": "A join combines rows from two or more tables based on a related column. INNER JOIN returns only matching rows. LEFT JOIN returns all rows from the left table and matching rows from right with NULL for non-matches. RIGHT JOIN is the opposite. FULL JOIN returns all rows from both tables. CROSS JOIN returns all combinations."
                },
                {
                    "question": "Difference between DELETE, TRUNCATE, and DROP?",
                    "expected_answer": "DELETE removes specific rows based on a WHERE condition and can be rolled back. TRUNCATE removes all rows quickly without logging individual deletions and cannot be rolled back in most databases. DROP deletes the entire table including its structure. DELETE is DML, TRUNCATE and DROP are DDL."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Write a SQL query to find the second highest salary.",
                    "expected_answer": "SELECT MAX(salary) FROM employees WHERE salary < (SELECT MAX(salary) FROM employees). Or use LIMIT with ORDER BY DESC LIMIT 1 OFFSET 1 in MySQL.",
                    "eval_type": "manual",
                    "test_cases": []
                },
                {
                    "question": "[CODING] Write a SQL query to find duplicate records.",
                    "expected_answer": "SELECT column, COUNT(*) FROM table GROUP BY column HAVING COUNT(*) > 1. Groups records and filters groups with more than one occurrence.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        },
        "medium": {
            "theory": [
                {
                    "question": "What are ACID properties?",
                    "expected_answer": "ACID stands for Atomicity meaning a transaction is all or nothing, Consistency meaning the database moves from one valid state to another, Isolation meaning concurrent transactions do not interfere with each other, and Durability meaning committed transactions persist even after system failure. ACID properties ensure reliable transaction processing."
                },
                {
                    "question": "What is indexing in databases?",
                    "expected_answer": "An index is a data structure that improves the speed of data retrieval at the cost of additional storage and slower writes. A B-tree index is the most common type. Indexes are created on columns frequently used in WHERE clauses and JOIN conditions. Without an index the database performs a full table scan which is slow on large tables."
                },
                {
                    "question": "What is a transaction?",
                    "expected_answer": "A transaction is a sequence of database operations treated as a single logical unit of work. It either completes entirely or fails entirely maintaining data integrity. Transactions are controlled using COMMIT to save changes, ROLLBACK to undo changes, and SAVEPOINT to set a point to rollback to within a transaction."
                },
                {
                    "question": "Explain different types of joins.",
                    "expected_answer": "INNER JOIN returns only rows where there is a match in both tables. LEFT OUTER JOIN returns all left table rows and matching right rows with NULL for non-matches. RIGHT OUTER JOIN is the reverse. FULL OUTER JOIN returns all rows from both tables with NULL for non-matches. SELF JOIN joins a table with itself for hierarchical data."
                },
                {
                    "question": "What is a view in SQL?",
                    "expected_answer": "A view is a virtual table based on the result of a SQL query. It does not store data physically but provides a saved query that can be treated like a table. Views simplify complex queries, provide security by limiting column access, and present data in a specific format without modifying underlying tables."
                },
                {
                    "question": "What is denormalization?",
                    "expected_answer": "Denormalization intentionally introduces redundancy into a normalized database to improve read performance. By combining tables we reduce the number of joins needed for queries. It trades storage space and write complexity for faster reads. Common in data warehouses and reporting databases where read performance is critical."
                },
                {
                    "question": "What are aggregate functions in SQL?",
                    "expected_answer": "Aggregate functions perform calculations on a set of rows returning a single value. COUNT counts rows, SUM adds values, AVG calculates average, MAX returns maximum, MIN returns minimum. They are used with GROUP BY to calculate aggregates per group and HAVING to filter groups after aggregation."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Write a SQL query using GROUP BY and HAVING.",
                    "expected_answer": "SELECT department, COUNT(*) as count FROM employees GROUP BY department HAVING COUNT(*) > 5. Groups by department and filters departments with more than 5 employees.",
                    "eval_type": "manual",
                    "test_cases": []
                },
                {
                    "question": "[CODING] Write a SQL query with INNER JOIN.",
                    "expected_answer": "SELECT e.name, d.department_name FROM employees e INNER JOIN departments d ON e.dept_id = d.dept_id. Combines employees and departments on matching department ID.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain database normalization forms.",
                    "expected_answer": "1NF requires atomic values and no repeating groups. 2NF requires 1NF and all non-key attributes depend on the entire primary key eliminating partial dependencies. 3NF requires 2NF and no transitive dependencies. BCNF is a stricter version of 3NF requiring every determinant to be a candidate key. Higher forms like 4NF and 5NF handle multi-valued and join dependencies."
                },
                {
                    "question": "What is a deadlock in databases?",
                    "expected_answer": "A deadlock occurs when two or more transactions are waiting for each other to release locks creating a circular dependency. For example transaction A holds lock on table X and waits for Y while transaction B holds Y and waits for X. Prevention includes lock ordering and timeouts. Detection algorithms rollback one transaction to break the cycle."
                },
                {
                    "question": "What is query optimization?",
                    "expected_answer": "Query optimization determines the most efficient way to execute a SQL query. The query optimizer generates multiple execution plans and selects the lowest cost one based on statistics. Techniques include using indexes, avoiding SELECT star, filtering early with WHERE clauses, and rewriting subqueries as joins to reduce computation."
                },
                {
                    "question": "Explain CAP theorem in databases.",
                    "expected_answer": "CAP theorem states a distributed database can guarantee only two of three: Consistency meaning all nodes see the same data, Availability meaning every request gets a response, and Partition Tolerance meaning the system works despite network failures. Traditional RDBMS favor CA. NoSQL databases like Cassandra favor AP and MongoDB favors CP."
                },
                {
                    "question": "What is database sharding?",
                    "expected_answer": "Sharding horizontally partitions data across multiple database instances called shards based on a shard key. Each shard contains a subset of the data. Sharding improves read and write throughput for large datasets but adds complexity in queries spanning multiple shards and makes joins and transactions harder to implement."
                },
                {
                    "question": "What is a stored procedure?",
                    "expected_answer": "A stored procedure is a precompiled set of SQL statements stored in the database. Benefits include reduced network traffic, improved performance from precompilation, reusability, and security by granting execute permission without granting table access. Created using CREATE PROCEDURE and called using EXEC or CALL."
                },
                {
                    "question": "Explain types of database locks.",
                    "expected_answer": "Shared locks allow multiple transactions to read simultaneously but prevent writes. Exclusive locks prevent other transactions from reading or writing. Intention locks indicate planned lower-level locks. Deadlocks occur when transactions hold locks and wait for each other. Lock granularity ranges from row-level giving more concurrency to table-level which is simpler."
                }
            ],
            "coding": [
                {
                    "question": "[CODING] Write a SQL query to rank employees by salary.",
                    "expected_answer": "SELECT name, salary, RANK() OVER (ORDER BY salary DESC) as rank FROM employees. Uses RANK window function to assign rank based on salary in descending order.",
                    "eval_type": "manual",
                    "test_cases": []
                }
            ]
        }
    },

    # ================= OPERATING SYSTEMS =================
    "os": {
        "easy": {
            "theory": [
                {
                    "question": "What is an operating system?",
                    "expected_answer": "An operating system is system software that manages computer hardware and software resources and provides common services for programs. It acts as an intermediary between users and hardware. Core functions include process management, memory management, file system management, device management, and security. Examples include Windows, Linux, and macOS."
                },
                {
                    "question": "What is a process?",
                    "expected_answer": "A process is a program in execution. It includes the program code, current activity represented by the program counter, registers, stack, heap, and data section. Each process has its own memory space. The OS manages processes through creation, scheduling, synchronization, communication, and termination. A process can have multiple threads sharing its resources."
                },
                {
                    "question": "What is a thread?",
                    "expected_answer": "A thread is the smallest unit of execution within a process. Multiple threads within the same process share memory space, file handles, and other resources but have their own program counter, registers, and stack. Threads are lighter than processes and context switching between threads is faster. Multithreading improves CPU utilization and responsiveness."
                },
                {
                    "question": "What is CPU scheduling?",
                    "expected_answer": "CPU scheduling decides which process runs next when the CPU is free. Scheduling algorithms include FCFS which runs in arrival order, SJF which runs the shortest job first, Round Robin which gives each process a fixed time quantum, and Priority Scheduling which runs highest priority processes first. Good scheduling maximizes CPU utilization and minimizes waiting time."
                },
                {
                    "question": "What is virtual memory?",
                    "expected_answer": "Virtual memory gives processes the illusion of having more memory than physically available by using disk space as an extension of RAM. Pages are loaded only when needed and swapped between RAM and disk. This allows running processes larger than physical memory and provides memory isolation between processes."
                },
                {
                    "question": "What is a deadlock?",
                    "expected_answer": "A deadlock occurs when a set of processes are blocked each waiting for a resource held by another. Four conditions are mutual exclusion, hold and wait, no preemption, and circular wait. Prevention removes one condition. Avoidance uses the Banker's algorithm. Detection and recovery allows deadlocks then resolves them by terminating or preempting a process."
                },
                {
                    "question": "What is the difference between process and thread?",
                    "expected_answer": "A process is an independent program with its own memory space and resources. A thread is a lightweight unit within a process sharing memory with other threads in the same process. Process creation is expensive while thread creation is cheap. Processes communicate via IPC while threads communicate through shared memory directly."
                }
            ],
            "coding": []
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain process scheduling algorithms.",
                    "expected_answer": "FCFS is simple but causes convoy effect where short processes wait behind long ones. SJF minimizes average waiting time but requires knowing burst time. SRTF is preemptive SJF. Round Robin gives equal time slices good for time-sharing. Priority scheduling can cause starvation solved by aging. Multilevel Queue has separate queues for different process categories."
                },
                {
                    "question": "What is paging?",
                    "expected_answer": "Paging divides physical memory into fixed-size frames and logical memory into same-size pages. The OS maintains a page table mapping logical page numbers to physical frame numbers. When a process accesses a page not in memory a page fault occurs and the page loads from disk. Paging eliminates external fragmentation but causes internal fragmentation."
                },
                {
                    "question": "What is segmentation?",
                    "expected_answer": "Segmentation divides memory into variable-size segments representing logical units like code, data, and stack. Each segment has a base address and limit. Segmentation matches the programmer's view of memory and allows different protection per segment. It suffers from external fragmentation. Modern systems often combine segmentation with paging."
                },
                {
                    "question": "What is inter-process communication?",
                    "expected_answer": "IPC allows processes to communicate and synchronize. Methods include pipes for one-directional communication, message queues for structured messages, shared memory for fastest communication, semaphores for synchronization, and sockets for network communication. Shared memory is fastest but requires synchronization to avoid race conditions."
                },
                {
                    "question": "Explain semaphores.",
                    "expected_answer": "A semaphore is a synchronization primitive using an integer variable accessed through wait and signal operations. A binary semaphore has values 0 and 1 used for mutual exclusion like a mutex. A counting semaphore controls access to a resource pool. Semaphores prevent race conditions when multiple processes access critical sections concurrently."
                },
                {
                    "question": "What is thrashing?",
                    "expected_answer": "Thrashing occurs when a process spends more time paging than executing because it lacks enough memory frames. The CPU is mostly handling page faults rather than useful work. Detected by high page fault rate and low CPU utilization. Solutions include adding physical memory, reducing multiprogramming degree, or using working set model to allocate sufficient frames."
                },
                {
                    "question": "What is a context switch?",
                    "expected_answer": "A context switch saves the state of a running process including registers, program counter, and memory pointers into its PCB and restores the state of the next scheduled process. Triggered by interrupts, system calls, or scheduler decisions. Has overhead since no useful work is done during switching. Thread context switches are cheaper than process context switches."
                }
            ],
            "coding": []
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain the Banker's algorithm.",
                    "expected_answer": "The Banker's algorithm avoids deadlocks by tracking available resources, maximum demand, current allocation, and remaining need for each process. Before granting a resource it checks if the resulting state is safe meaning there exists a sequence where all processes can finish. If the state is unsafe the request is denied until it can be safely granted."
                },
                {
                    "question": "What is the difference between preemptive and non-preemptive scheduling?",
                    "expected_answer": "In preemptive scheduling the OS can forcibly remove the CPU from a running process to give to a higher-priority or shorter process. Examples are SRTF and Round Robin. In non-preemptive scheduling a process runs until it voluntarily releases the CPU. FCFS and non-preemptive SJF are examples. Preemptive is better for interactive systems but has more context switch overhead."
                },
                {
                    "question": "Explain page replacement algorithms.",
                    "expected_answer": "FIFO replaces the oldest page and suffers from Belady's anomaly where more frames can cause more faults. LRU replaces the least recently used page and is near-optimal but expensive to implement. Optimal replaces the page not needed for the longest time in future but requires future knowledge. Clock algorithm approximates LRU using a reference bit efficiently."
                },
                {
                    "question": "What is a mutex?",
                    "expected_answer": "A mutex is a mutual exclusion lock ensuring only one thread enters a critical section at a time. A thread acquires the mutex before entering and releases it after. If the mutex is held another thread blocks until released. Unlike semaphores a mutex must be released by the same thread that acquired it preventing certain bugs."
                },
                {
                    "question": "Explain memory allocation strategies.",
                    "expected_answer": "First Fit allocates the first free block large enough and is fast but fragments the start of memory. Best Fit allocates the smallest sufficient block minimizing waste but leaves many tiny unusable fragments. Worst Fit allocates the largest block leaving the largest remaining fragment. Buddy System splits memory into power-of-two blocks allowing efficient merging of adjacent free blocks."
                },
                {
                    "question": "What is the producer-consumer problem?",
                    "expected_answer": "The producer-consumer problem is a classic synchronization problem where producers generate data into a shared bounded buffer and consumers take data from it. Problems arise if producer adds to a full buffer or consumer takes from an empty one. Solved using three semaphores: full counts filled slots, empty counts free slots, and mutex ensures exclusive buffer access."
                },
                {
                    "question": "What is demand paging?",
                    "expected_answer": "Demand paging loads pages into memory only when they are accessed rather than loading the entire process at startup. When a process accesses a missing page a page fault interrupt occurs. The OS finds the page on disk, loads it into a free frame, updates the page table, and resumes execution. Reduces initial loading time and memory usage but adds page fault overhead."
                }
            ],
            "coding": []
        }
    },

    # ================= COMPUTER NETWORKS =================
    "cn": {
        "easy": {
            "theory": [
                {
                    "question": "What is the OSI model?",
                    "expected_answer": "The OSI model divides network communication into 7 layers: Physical which transmits raw bits, Data Link which handles frames and MAC addresses, Network which handles routing and IP addresses, Transport which manages end-to-end communication using TCP and UDP, Session which manages sessions, Presentation which handles encryption and formatting, and Application which provides network services to user applications."
                },
                {
                    "question": "What is TCP/IP?",
                    "expected_answer": "TCP/IP is the foundational protocol suite of the internet. TCP is connection-oriented providing reliable ordered delivery with error checking. IP is connectionless handling addressing and routing. The TCP/IP model has four layers: Network Access, Internet, Transport, and Application. It is the actual standard used on the internet unlike the theoretical OSI model."
                },
                {
                    "question": "What is the difference between TCP and UDP?",
                    "expected_answer": "TCP is connection-oriented providing reliable ordered delivery with error checking and flow control using a three-way handshake. UDP is connectionless providing fast unreliable delivery without guarantees. TCP is used for web browsing and email where accuracy matters. UDP is used for video streaming and gaming where speed is more important than reliability."
                },
                {
                    "question": "What is an IP address?",
                    "expected_answer": "An IP address is a unique numerical label assigned to each device on a network. IPv4 uses 32-bit addresses in dotted decimal notation like 192.168.1.1. IPv6 uses 128-bit addresses supporting vastly more devices. IP addresses identify both the host and the network. Private IPs are used within local networks and public IPs on the internet."
                },
                {
                    "question": "What is DNS?",
                    "expected_answer": "DNS stands for Domain Name System. It translates human-readable domain names like google.com into IP addresses. Resolution involves querying a recursive resolver which checks root servers, TLD servers, and authoritative name servers. DNS caching reduces lookup time. Without DNS users would need to memorize IP addresses to access websites."
                },
                {
                    "question": "What is HTTP and HTTPS?",
                    "expected_answer": "HTTP is the HyperText Transfer Protocol for transferring data between browsers and servers following a stateless request-response model. HTTPS adds SSL/TLS encryption protecting data in transit. HTTPS prevents eavesdropping and man-in-the-middle attacks. Modern websites use HTTPS for security and search engine ranking advantages."
                },
                {
                    "question": "What is a router vs a switch?",
                    "expected_answer": "A router operates at the Network layer directing packets between different networks using IP addresses connecting a home network to the internet. A switch operates at the Data Link layer connecting devices within the same network using MAC addresses. Switches forward frames to specific MAC addresses while routers make intelligent routing decisions between networks."
                }
            ],
            "coding": []
        },
        "medium": {
            "theory": [
                {
                    "question": "Explain the TCP three-way handshake.",
                    "expected_answer": "The three-way handshake establishes a TCP connection. First the client sends SYN with its initial sequence number. Second the server responds with SYN-ACK acknowledging the client's SYN and including its own sequence number. Third the client sends ACK acknowledging the server's SYN. After this the connection is established and bidirectional data transfer can begin."
                },
                {
                    "question": "What is subnetting?",
                    "expected_answer": "Subnetting divides a large network into smaller sub-networks using a subnet mask. The subnet mask determines which bits represent the network and which represent the host. CIDR notation like 192.168.1.0/24 indicates 24 bits for network. Subnetting improves security, reduces broadcast traffic, and allows efficient IP address usage."
                },
                {
                    "question": "What is a MAC address?",
                    "expected_answer": "A MAC address is a unique hardware identifier assigned to a network interface card. It is 48 bits represented as six hexadecimal pairs like 00:1A:2B:3C:4D:5E. The first three bytes identify the manufacturer and the last three are device-specific. MAC addresses operate at the Data Link layer and are used for local network communication within a subnet."
                },
                {
                    "question": "Explain NAT.",
                    "expected_answer": "Network Address Translation maps private IP addresses to a single public IP address when packets leave the local network. This allows multiple devices with private IPs to share one public IP conserving the limited IPv4 address space. The NAT router maintains a translation table. Port Address Translation maps each connection to a unique port on the public IP."
                },
                {
                    "question": "What is a firewall?",
                    "expected_answer": "A firewall monitors and controls incoming and outgoing network traffic based on security rules. Packet filtering firewalls examine packet headers. Stateful firewalls track connection state. Application layer firewalls inspect packet contents. Firewalls protect against unauthorized access and malicious traffic by blocking suspicious connections and enforcing network policies."
                },
                {
                    "question": "What is DHCP?",
                    "expected_answer": "DHCP stands for Dynamic Host Configuration Protocol. It automatically assigns IP addresses, subnet masks, default gateway, and DNS server information to devices. The process involves DISCOVER, OFFER, REQUEST, and ACKNOWLEDGE messages. DHCP eliminates manual IP configuration and manages address allocation efficiently from a pool of available addresses."
                },
                {
                    "question": "Explain the difference between HTTP/1.1 and HTTP/2.",
                    "expected_answer": "HTTP/1.1 opens connections per request or uses persistent connections but sends requests sequentially causing head-of-line blocking. HTTP/2 uses multiplexing allowing multiple requests simultaneously over one connection using binary framing. HTTP/2 also supports header compression using HPACK and server push reducing latency significantly for pages with many resources."
                }
            ],
            "coding": []
        },
        "hard": {
            "theory": [
                {
                    "question": "Explain routing protocols.",
                    "expected_answer": "RIP is a distance-vector protocol using hop count as metric with maximum 15 hops suitable for small networks. OSPF is a link-state protocol using Dijkstra's algorithm suitable for large networks. BGP is the path-vector protocol for internet routing between autonomous systems. Link-state protocols like OSPF converge faster than distance-vector protocols like RIP."
                },
                {
                    "question": "What is SSL/TLS?",
                    "expected_answer": "TLS provides secure communication using asymmetric encryption for key exchange and symmetric encryption for data transfer. The handshake involves the server sending its certificate, client verifying it, both agreeing on encryption algorithms, and exchanging session keys. TLS ensures confidentiality, integrity, and authentication preventing eavesdropping and tampering."
                },
                {
                    "question": "What is the difference between IPv4 and IPv6?",
                    "expected_answer": "IPv4 uses 32-bit addresses supporting about 4 billion unique addresses which are nearly exhausted. IPv6 uses 128-bit addresses providing virtually unlimited addresses. IPv6 also improves header format for faster routing, has built-in IPSec for security, supports autoconfiguration, and eliminates the need for NAT. IPv6 addresses use hexadecimal notation with colons."
                },
                {
                    "question": "Explain congestion control in TCP.",
                    "expected_answer": "TCP congestion control prevents overwhelming the network. Slow Start begins with a small window doubling each RTT until reaching the threshold. Congestion Avoidance increases the window linearly after the threshold. When loss is detected the threshold halves. Fast Retransmit retransmits lost segments on three duplicate ACKs without waiting for timeout."
                },
                {
                    "question": "What is a VPN?",
                    "expected_answer": "A VPN creates an encrypted tunnel over a public network for secure remote access. It uses protocols like IPSec, OpenVPN, or WireGuard. VPNs provide privacy by masking IP addresses, security by encrypting data, and allow accessing corporate networks or region-restricted content remotely. Site-to-site VPNs connect entire office networks together."
                },
                {
                    "question": "Explain the concept of network topologies.",
                    "expected_answer": "Bus topology connects all devices to a single cable causing collisions and single point of failure. Star topology connects to a central switch providing easy management but switch failure affects all. Ring topology connects devices in a circle. Mesh topology connects every device to every other providing redundancy but is expensive. Hybrid combines multiple topologies."
                },
                {
                    "question": "What is Quality of Service in networking?",
                    "expected_answer": "QoS allocates network resources appropriately for different traffic types. It prioritizes critical traffic like voice and video over less time-sensitive traffic like file downloads. Mechanisms include traffic classification, queuing algorithms like weighted fair queuing, traffic shaping to smooth bursts, and policing to limit rates. QoS prevents one application from monopolizing bandwidth."
                }
            ],
            "coding": []
        }
    }
}