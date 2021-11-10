import React, { Component } from 'react';

export function UnitRow() {
    return(
        <div className="d-flex flex-row">
            {UnitAttributeList()}
        </div>
    )
}

export function UnitAttribute(props) {
    return(
        <div className="ml-1 mr-1">{props.message}</div>
    )
}

export function UnitAttributeList() {
    let array = [1,2,3,4,5,6,7,8,9,10];
    let attributeArray = array.map((number) => {
        let component = <UnitAttribute message = {number}></UnitAttribute>;
        return component;
    })
    return attributeArray;
}