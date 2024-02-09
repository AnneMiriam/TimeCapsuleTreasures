import React, { useEffect, useState } from 'react';
import CollectionForm from '../components/CollectionForm';
import CollectionContainer from '../components/CollContainer';

    // Show all of a users collections cards
    // New Collection Form

function User() {
    const [collections, setCollections] = useState([]);

    useEffect(() => {
        fetch('/api/collections')
        .then(r => r.json())
        .then(setCollections)
    },[])

    function addNewCltn(newCollection) {
        setCollections([...collections, newCollection])
    }

    function removeCollection(id) {
        setCollections(collections.filter(collection => collection.id !== id))
    }

    return (
        <>
            <CollectionContainer 
                collections={collections} 
                removeCollection={removeCollection} 
            />
            <CollectionForm handleNewCltn={addNewCltn} /> 
        </>
    )
}

export default User;