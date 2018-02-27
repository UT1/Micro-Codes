Micro codes for checking the Pandas


### Read CSV in chunks
data_read = pd.read_csv('Filename.csv',chunksize=x,encoding = "any encoding format for eg :ISO-8859-1")      
data = pd.concat(data_read,ignore_index=True)    

### Split the dataframe based on the numeric and categorical values 

###	Numeric Split
cleansed_data_numeric = data.select_dtypes(include=['number']).columns
data_read_numeric = data.loc[:,lambda data : cleansed_data_numeric]
numeric_null_count = data_read_numeric.apply(lambda x : sum(x.notnull()))

### 	Categorical Split
cleansed_data_category = data.select_dtypes(exclude=['number']).columns
data_read_category = data.loc[:,lambda data : cleansed_data_category]
categorical_null_count = data_read_category.apply(lambda x : sum(x.notnull()))

### Date Difference and Date Conversion Logic
import datetime as DT
	data['Date'].dtype
	#pd.to_datetime(data['Date']) 
now = pd.Timestamp(DT.datetime.now())
data['Date'] = pd.to_datetime(data['Date'], format='%m/%d/%Y') 

### Difference
data['DOB_NEW'] =data['DOB_NEW'].where(data['DOB_NEW'] < now, data['DOB_NEW'] -  np.timedelta64(100, 'Y'))   # 2
data['Age_Driver1'] = (now - data['DOB_NEW']).astype('<m8[Y]')    # 3

### Copying chunks of data from one frame to another 
### data=original frame ptsdriver2 = copied frame
ptsdriver2 = data[['ViolPoints2Driver_2',
'ViolPoints1Driver_2',
'ViolPoints3Driver_2',
'ViolPoints4Driver_2',
'ViolPoints5Driver_2',
'ViolPoints6Driver_2',
'ViolPoints7Driver_2',
'ViolPoints8Driver_2',
]].copy()
 
### Sum of values in the frame row-wise
ptsdriver2['Points_Driver2'] = ptsdriver2.apply(lambda x : x.sum(),axis=1)

### Replace Blank values with NaN 
dataframe.replace(r'^\s*$', np.NaN, regex=True, inplace = True)

### Scaling the values to remove if you want to treat numeric values on same scale 
### Libraries
from sklearn.preprocessing import StandardScaler
Step1 : Create Scale_clean using
Example : 
scale_clean = StandardScaler().fit(data[['Zip']])
Step2 :  Create Clean transform 
Example : 
clean_transform = scale_clean.transform(data[['Zip']])
Step3 : Create dataframe of the Clean Transform
Example : clean = pd.DataFrame(clean_transform)
Step4 : Join/Concatenate the Frames
frames = [data,clean]
data = pd.concat(frames,axis=1)
Step4 : Drop the Original Columns and Rename the New Ones 
data = data.drop(['Zip'],1)
data = data.rename(columns={0:'Zip'})
   

###Copying the data in a different frame based on column value condition

datax = data[data['Gender']=='M'] 
