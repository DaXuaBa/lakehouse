import React, { useState, useEffect } from 'react';
import { useDispatch } from 'react-redux';
import { useLocation } from 'react-router-dom';
import { connect } from '../actions/userActions';
import { Button } from 'react-bootstrap';

const StravaConnectedPage = () => {
  const [isConnected, setIsConnected] = useState(false);
  const location = useLocation();

  useEffect(() => {
    const userInfoFromLocalStorage = localStorage.getItem('userInfo');
    const userInfoObject = JSON.parse(userInfoFromLocalStorage);

    const stravaInfo = userInfoObject?.Strava;

    setIsConnected(stravaInfo !== null);
  }, [location]);

  const STRAVA_CLIENT_ID = 116867
    const STRAVA_REPONSE_TYPE = "code"
    const STRAVA_REDIRECT_URI = "http://localhost:3000/connectstrava"
    const STRAVA_APPROVAL_PROMPT = "force"
    const STRAVA_SCOPE = "read"
    const STRAVA_ACTIVATY = "read_all"
    const URL = `https://www.strava.com/oauth/authorize?client_id=${STRAVA_CLIENT_ID}&response_type=${STRAVA_REPONSE_TYPE}&redirect_uri=${STRAVA_REDIRECT_URI}&approval_prompt=${STRAVA_APPROVAL_PROMPT}&scope=${STRAVA_SCOPE},activity:${STRAVA_ACTIVATY}`;

    const dispatch = useDispatch();

    const [code, setCode] = useState(null);

    useEffect(() => {
        const urlSearchParams = new URLSearchParams(location.search);
        const newCode = urlSearchParams.get('code');
    
        if (newCode !== code) {
          setCode(newCode);
        }
      }, [location.search, code]);    
    
    useEffect(() => {
        if (code) {
            dispatch(connect(code));

            const userInfoFromLocalStorage = localStorage.getItem('userInfo');
            const userInfoObject = JSON.parse(userInfoFromLocalStorage);
            userInfoObject.Strava = 'connected';
            localStorage.setItem('userInfo', JSON.stringify(userInfoObject));

            setIsConnected(true);
        }

    }, [code, dispatch]);

  return (
    <div style={{ textAlign: 'center', padding: '20px' }}>
      <div
        style={{
          backgroundColor: '#e3e3e3',
          borderRadius: '10px',
          padding: '20px',
        }}
      >
        {isConnected ? (
          <>
            <h1 style={{ color: 'green' }}>Đã kết nối với Strava!</h1>
            <p>Tài khoản của bạn đã kết nối rồi.</p>
          </>
        ) : (
          <>
            <h1 style={{ color: 'red' }}>Chưa kết nối với Strava</h1>
            <p>
              Để bắt đầu, hãy nhấp vào nút bên dưới để kết nối với tài khoản Strava của bạn.
            </p>
            <Button
              style={{
                backgroundColor: 'blue',
                color: 'white',
                padding: '10px 20px',
                borderRadius: '5px',
                cursor: 'pointer',
              }}
                variant="primary"
                href={URL}
                target="_blank"
                rel="noopener noreferrer"
            >
                Kết nối tới Strava
            </Button>
          </>
        )}
      </div>
    </div>
  );
};

export default StravaConnectedPage;
