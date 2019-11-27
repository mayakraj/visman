#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 16:18:42 2019
@author: akshay72

Main file running the application.
"""
import psycopg2, config_parser
from flask import Flask, request, jsonify
import pandas as pd
import db_config.dbManager as dbm
import logging
logging.basicConfig(level = logging.INFO)

from datetime import datetime

start_time = ""
end_time = ""

app = Flask(__name__)
params = config_parser.config(filename='db_config/database.ini', section='postgresql')
queries = config_parser.config(filename='db_config/database.ini', section='queries')


def replace(data):
    if data is not None:
        return data
    data = None
    return data


def generate(first,last):
    return first+last


@app.route('/', methods=['GET', 'POST'])
def hello_worlds():
    return "<div><b>Sorry!!<br/>Only team has access to database<b><a href='/about'>About</a></div>"


@app.route('/about', methods=['GET', 'POST'])
def about():
    return jsonify({'Company': 'Visitor Management',
                    'Dev center': 'Team Foundation',
                    'version': 'heroku test development'})


@app.route('/society_info', methods=['GET', 'POST'])
def society_info():
    """ Gives the society id and society name for all registered society."""
    try:
        query = queries['society_info']

        with dbm.dbManager() as manager:
            result = manager.getDataFrame(query)
            logging.info(result)
            logging.info(result.to_dict(orient='records'))
        return jsonify(result.to_dict(orient='records'))

    except psycopg2.DatabaseError as error:
        errors = {'society info': False, 'error': error}
        return str(errors)


@app.route('/society_register', methods=['GET', 'POST'])
def society_register():
    """Register society"""
    try:
        # society details
        regd_no = request.form['regd_no']
        society_name = request.form['society_name']
        society_address = request.form['society_address']
        total_buildings = request.form['total_buildings']
        total_flats = request.form['total_flats']

        df = pd.DataFrame({'regd_no': regd_no, 'society_name': society_name, 'society_address': society_address,
                           'total_buildings': total_buildings, 'total_flats': total_flats}, index=[0])

        with dbm.dbManager() as manager:
            manager.commit(df, 'visitor_management_schema.society_table')
        # first user details
        return "Society registered successfully"
    except psycopg2.DatabaseError as error:
        errors = {'society registeration': False,
                  'error': (error)
                  }
        return str(errors)


@app.route('/get_id', methods=['GET', 'POST'])
def get_id():
    """ get the society id by passing the society registration."""
    try:
        regd_no = request.form['regd_no']
        query_society_id = queries['get_society_id']
        query = query_society_id.format(regd_no)
        
        with dbm.dbManager() as manager:
            result = manager.getDataFrame(query)

        return jsonify(result.to_dict(orient='records'))
    except psycopg2.DatabaseError as error:
        errors = {'registeration': False, 'error': (error) }
        return str(errors)


@app.route('/get_wing_list', methods=['GET', 'POST'])
def get_wing_list():
    """get list of wings from a Society"""
    try:
        society_id = request.form['society_id']
        society_wing_list = queries['get_society_wing_list']
        query = society_wing_list.format(society_id)

        with dbm.dbManager() as manager:
            result = manager.getDataFrame(query)
        return jsonify(result.to_dict(orient='records'))
    except psycopg2.DatabaseError as error:
        errors = {'get_wing_list': False, 'error': (error)}
        return str(errors)


@app.route('/get_flat_list', methods=['GET', 'POST'])
def get_flat_list():
    try:
        society_id = request.form['society_id']
        wing_name = request.form['wing_name']
        wing_flats_list = queries['get_flat_list']
        query = wing_flats_list.format(society_id, wing_name)

        with dbm.dbManager() as manager:
            result = manager.getDataFrame(query)

        return jsonify(result.to_dict(orient='records'))
    except psycopg2.DatabaseError as error:
        errors = {'get_flat_list': False, 'error': (error)}
        return str(errors)


@app.route('/add_flat', methods=['GET', 'POST'])
def add_flat():
    """Add details of Flat if Flat not Present"""
    try:
        society_id = request.form['society_id']
        wing_name = request.form['wing_name']
        flat_no = request.form['flat_no']

        df = pd.DataFrame({'society_id': str(society_id), 'wing': str(wing_name), 'flat_no': str(flat_no)}, index=[0])

        with dbm.dbManager() as manager:
            manager.commit(df, 'visitor_management_schema.flat_details')
            success = True
            return jsonify(success)
            #return jsonify(q)

    except psycopg2.DatabaseError as error:
        errors = {'get_wing_list': False, 'error': (error)}
        return str(errors)


@app.route('/get_flat_id', methods=['GET', 'POST'])
def get_flat_id():
    """get flat id by giving the society and flat no and wing name"""
    society_id = request.form['society_id']
    wing_name = request.form['wing_name']
    flat_no = request.form['flat_no']
    query_flat_id = queries['get_flat_id_query']

    query = query_flat_id.format(society_id, wing_name, flat_no)

    with dbm.dbManager() as manager:
        result = manager.getDataFrame(query)

    return jsonify(result.to_dict(orient='records'))



@app.route('/user/register', methods=['GET','POST'])
def user_register():
    """staff Registeration (staff may be watchman or secretary)"""
    # username=request.form['username']
    email = request.form['email']
    first_name = request.form['first_name']
    middle_name = request.form['middle_name']
    last_name = request.form['last_name']
    password = request.form['password']
    society_id = request.form['society_id']
    flat_id = request.form['flat_id']
    isadmin = request.form['isadmin']
    user_entity = request.form['user_entity']
    username = request.form['email']

    try:

        df = pd.DataFrame({'username': str(username),
                           'email': str(email),
                           'first_name': str(first_name),
                           'middle_name': str(middle_name),
                           'last_name': str(last_name),
                           'password': str(password),
                           'society_id': str(society_id),
                           'isadmin': str(isadmin),
                           'flat_id': str(flat_id),
                           'user_entity': str(user_entity)
                           },
                          index=[0])

        with dbm.dbManager() as manager:
            manager.commit(df, 'visitor_management_schema.user_table')
        return "User registered Succesfully"
    except psycopg2.DatabaseError as error:
        errors = {'registeration': False, 'error': error}
        return str(errors)


#staff Login
@app.route('/user/login', methods=['GET', 'POST'])
def login():
    validate_query = queries['validate_user']
    
    username = request.form['username']
    password = request.form['password']
    postgres_user_login_query = validate_query.format(username,password)
    
    with dbm.dbManager() as manager:
            result = manager.getDataFrame(postgres_user_login_query)

    return jsonify(result.to_dict(orient='records'))
    

# visitor entry from staff
@app.route('/insertVisitor', methods=['GET','POST'])
def insertVisitor():
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    contact_number = request.form['contact_number']
    entry_time = request.form['entry_time']
    # entry_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    flat_id = request.form['flat_id']
    staff_id = request.form['staff_id']
    visit_reason = request.form['visit_reason']
    society_id = request.form['society_id']
    photo = request.form['photo']

    tuple_insert = ('{}'.format(first_name), '{}'.format(last_name), '{}'.format(contact_number),
                    '{}'.format(entry_time),
                    '{}'.format(flat_id), '{}'.format(staff_id), '{}'.format(visit_reason), '{}'.format(society_id),
                    '{}'.format(photo))
    try:
        with dbm.dbManager() as manager:
            #value = manager.commit(df, 'visitor_management_schema.visitor_table')
            visitor_id = manager.callprocedure('visitor_management_schema.insertvisitor',tuple_insert)
            logging.info('Visitor details entered successfully')
            return jsonify(visitor_id)

    except psycopg2.DatabaseError as error:
        errors = {'visitor_entry': False,
                      'error': (error)
                      }
        return str(errors)

@app.route('/update_exit',methods=['GET','POST'])
def update_exit():
    #update_exit=queries['update_exit']
    visitor_id=request.form['id']
    exit_time=request.form['exit_time']
    try:
        update_query='''update visitor_management_schema.visitor_table set exit_time='{}' where id={}'''.format(exit_time,visitor_id)
        
        with dbm.dbManager() as manager:
            manager.updateDB(update_query)
        success=True
    except:
        success=False
    return jsonify(success)
        

# admin access
@app.route('/dashboard_count', methods=['GET','POST'])
def dashboard_count():
    try:
        society_id = request.form['society_id']
        query_society_id = queries['visitor_and_watchman_cnt']
        query = query_society_id.format(society_id)

        with dbm.dbManager() as manager:
            result = manager.getDataFrame(query)

        return jsonify(result.to_dict(orient='records'))
    except psycopg2.DatabaseError as error:
        errors = {'registeration': False, 'error': (error)}
        return str(errors)



#admin access
@app.route('/dashboard_watchman', methods=['GET', 'POST'])
def dashboard_watchman():
    society_id = request.form['society_id']
    query_society_staff = queries['society_staff_list']

    query  = query_society_staff.format(society_id)
    
    with dbm.dbManager() as manager:
        result = manager.getDataFrame(query)
        #result_Data = result.to_json(orient='values')
        
    return jsonify(result.to_dict(orient='records'))


@app.route('/dashboard_members', methods=['GET', 'POST'])
def dashboard_members():
    society_id = request.form['society_id']
    query_society_staff = queries['society_members_list']

    query = query_society_staff.format(society_id)

    with dbm.dbManager() as manager:
        result = manager.getDataFrame(query)

    return jsonify(result.to_dict(orient='records'))

@app.route('/dashboard_visitor', methods=['GET', 'POST'])
def dashboard_visitor():
    society_id = request.form['society_id']
    all_visitor_details = queries['all_visitor_details3']
    query_visitor_list = all_visitor_details.format(society_id)
    
    with dbm.dbManager() as manager:
        result = manager.getDataFrame(query_visitor_list)

    return jsonify(result.to_dict(orient='records'))


@app.route('/set_user_login_status', methods=['GET', 'POST'])
def set_user_login_status():
    user_id=request.form['user_id']
    user_status=request.form['user_status']
    logging.info('Setting User id: %s status set to %s', user_id, user_status)
    query_approve_user = queries['user_status']
    logging.info('query generated %s', query_approve_user)
    set_approve_user_query = query_approve_user.format(user_status, user_id)
    with dbm.dbManager() as manager:
        result = manager.updateDB(set_approve_user_query)
        logging.info('User id: %s status set to %s', user_id, user_status)
        logging.info('result =  %s', result)
        print(result)
        return jsonify(bool(request))




#app.run(debug=True)